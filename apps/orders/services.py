from decimal import Decimal
from django.db import transaction
from django.utils import timezone
from apps.orders.models import Order, OrderItem, SellerOrder, Invoice
from apps.cart.services import CartService
from apps.inventory.services import InventoryService
from common.mixins import generate_order_number, generate_invoice_number


class OrderService:
    @staticmethod
    @transaction.atomic
    def create_order(buyer, billing_address_id, shipping_address_id, notes=''):
        cart_items = CartService.get_cart_items(buyer).select_related(
            'seller', 'variant__product'
        ).prefetch_related('variant__images', 'seller__pricing')
        if not cart_items.exists():
            raise ValueError('Cart is empty')

        subtotal = Decimal('0.00')
        total_tax = Decimal('0.00')
        total_shipping = Decimal('0.00')

        from apps.pricing.models import SellerPricing
        from apps.pricing.services import PricingService

        # Validate pricing, MOQ, and stock before proceeding
        for item in cart_items:
            try:
                pricing = SellerPricing.objects.get(
                    seller=item.seller,
                    variant=item.variant,
                    is_active=True,
                )
            except SellerPricing.DoesNotExist:
                raise ValueError(f'Product {item.variant.product.name} is no longer available. Please remove it from your cart.')

            if item.quantity < pricing.minimum_order_quantity:
                raise ValueError(f'Minimum order for {item.variant.product.name} is {pricing.minimum_order_quantity}. Please update your cart.')

            current_price = PricingService.get_price_for_quantity(pricing, item.quantity)
            if item.unit_price != current_price:
                # Update the cart item to reflect new pricing so user sees it next time
                item.unit_price = current_price
                item.tax_rate = pricing.tax_rate
                item.shipping_charge = Decimal('0.00') if pricing.free_shipping else pricing.shipping_charge
                item.save(update_fields=['unit_price', 'tax_rate', 'shipping_charge'])
                raise ValueError(f'The price for {item.variant.product.name} has changed. Your cart has been updated. Please review before checking out.')

            # Check stock explicitly before reserving
            inventory = item.variant.inventory.filter(seller=item.seller).first()
            if not inventory or inventory.available_stock < item.quantity:
                raise ValueError(f'Insufficient stock for {item.variant.product.name}.')

        for item in cart_items:
            subtotal += item.total_price
            tax_amount = item.unit_price * item.quantity * item.tax_rate / 100
            total_tax += tax_amount
            if not item.seller.pricing.filter(variant=item.variant, free_shipping=True).exists():
                total_shipping += item.shipping_charge

        total_amount = subtotal + total_tax + total_shipping

        order = Order.objects.create(
            order_number=generate_order_number(),
            buyer=buyer,
            billing_address_id=billing_address_id,
            shipping_address_id=shipping_address_id,
            subtotal=subtotal,
            total_tax=total_tax,
            total_shipping=total_shipping,
            total_amount=total_amount,
            notes=notes,
        )

        seller_orders = {}
        for cart_item in cart_items:
            tax_amount = cart_item.unit_price * cart_item.quantity * cart_item.tax_rate / 100

            # Honor free shipping the same way the order-level total does above, so
            # the per-seller order (and its invoice) totals match Order.total_shipping.
            is_free_shipping = cart_item.seller.pricing.filter(
                variant=cart_item.variant, free_shipping=True
            ).exists()
            item_shipping = Decimal('0.00') if is_free_shipping else cart_item.shipping_charge

            product_image = None
            primary_img = cart_item.variant.images.filter(is_primary=True).first()
            if primary_img:
                product_image = primary_img.image_url
            else:
                first_img = cart_item.variant.images.first()
                if first_img:
                    product_image = first_img.image_url

            order_item = OrderItem.objects.create(
                order=order,
                seller=cart_item.seller,
                variant=cart_item.variant,
                product_name=cart_item.variant.product.name,
                variant_name=cart_item.variant.name,
                product_image=product_image,
                quantity=cart_item.quantity,
                unit_price=cart_item.unit_price,
                tax_rate=cart_item.tax_rate,
                tax_amount=tax_amount,
                shipping_charge=item_shipping,
                total_price=cart_item.total_price,
            )

            seller_id = str(cart_item.seller.id)
            if seller_id not in seller_orders:
                seller_orders[seller_id] = {
                    'seller': cart_item.seller,
                    'subtotal': Decimal('0.00'),
                    'total_tax': Decimal('0.00'),
                    'total_shipping': Decimal('0.00'),
                }
            seller_orders[seller_id]['subtotal'] += cart_item.total_price
            seller_orders[seller_id]['total_tax'] += tax_amount
            seller_orders[seller_id]['total_shipping'] += item_shipping

            # Reserve stock
            inventory = cart_item.variant.inventory.filter(seller=cart_item.seller).first()
            if inventory:
                InventoryService.reserve_stock(inventory, cart_item.quantity)

        for seller_id, data in seller_orders.items():
            SellerOrder.objects.create(
                order=order,
                seller=data['seller'],
                subtotal=data['subtotal'],
                total_tax=data['total_tax'],
                total_shipping=data['total_shipping'],
                total_amount=data['subtotal'] + data['total_tax'] + data['total_shipping'],
            )

        # Clear cart
        CartService.clear_cart(buyer)

        return order

    @staticmethod
    def confirm_order(order):
        order.status = 'confirmed'
        order.save(update_fields=['status', 'updated_at'])
        order.items.update(status='confirmed')
        order.seller_orders.update(status='confirmed')
        return order

    @staticmethod
    def cancel_order(order, reason=''):
        if order.status in ['shipped', 'delivered', 'cancelled']:
            raise ValueError(f'Cannot cancel order because it is already {order.status}')
        order.status = 'cancelled'
        order.cancellation_reason = reason
        order.cancelled_at = timezone.now()
        order.save(update_fields=['status', 'cancellation_reason', 'cancelled_at', 'updated_at'])
        order.items.update(status='cancelled')

        # Release reserved stock
        for item in order.items.all():
            inventory = item.variant.inventory.filter(seller=item.seller).first()
            if inventory:
                InventoryService.release_stock(inventory, item.quantity)

        return order

    @staticmethod
    def ship_order(seller_order, tracking_number=None, tracking_url=None):
        if seller_order.status in ['shipped', 'delivered', 'cancelled']:
            raise ValueError(f'Cannot ship order that is already {seller_order.status}')
        
        seller_order.status = 'shipped'
        seller_order.tracking_number = tracking_number
        seller_order.tracking_url = tracking_url
        seller_order.shipped_at = timezone.now()
        seller_order.save()

        # Deduct fulfilled stock permanently
        order_items = seller_order.order.items.filter(seller=seller_order.seller)
        for item in order_items:
            inventory = item.variant.inventory.filter(seller=item.seller).first()
            if inventory:
                InventoryService.fulfill_stock(inventory, item.quantity)

        # Check if all seller orders are shipped
        order = seller_order.order
        if all(so.status == 'shipped' for so in order.seller_orders.all()):
            order.status = 'shipped'
            order.save(update_fields=['status', 'updated_at'])

        return seller_order

    @staticmethod
    def deliver_order(seller_order):
        if seller_order.status in ['delivered', 'cancelled']:
            raise ValueError(f'Cannot deliver order that is already {seller_order.status}')
        if seller_order.status != 'shipped':
            raise ValueError('Order must be shipped before it can be delivered')
            
        seller_order.status = 'delivered'
        seller_order.delivered_at = timezone.now()
        seller_order.save()

        # Check if all seller orders are delivered
        order = seller_order.order
        if all(so.status == 'delivered' for so in order.seller_orders.all()):
            order.status = 'delivered'
            order.delivered_at = timezone.now()
            order.save(update_fields=['status', 'delivered_at', 'updated_at'])

            # Create invoices
            for so in order.seller_orders.all():
                Invoice.objects.create(
                    invoice_number=generate_invoice_number(),
                    order=order,
                    seller_order=so,
                    seller=so.seller,
                    buyer=order.buyer,
                    subtotal=so.subtotal,
                    total_tax=so.total_tax,
                    total_amount=so.total_amount,
                    status='generated',
                    issued_at=timezone.now(),
                )

        return seller_order

    @staticmethod
    def get_buyer_orders(buyer, status=None):
        queryset = Order.objects.filter(buyer=buyer, deleted_at__isnull=True)
        if status:
            queryset = queryset.filter(status=status)
        return queryset

    @staticmethod
    def get_seller_orders(seller, status=None):
        queryset = SellerOrder.objects.filter(seller=seller)
        if status:
            queryset = queryset.filter(status=status)
        return queryset
