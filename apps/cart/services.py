from django.db import transaction
from apps.cart.models import Cart, CartItem
from apps.pricing.models import SellerPricing
from apps.pricing.services import PricingService
from apps.inventory.models import Inventory


class CartService:
    @staticmethod
    def get_cart(buyer):
        cart, _ = Cart.objects.get_or_create(buyer=buyer)
        return cart

    @staticmethod
    def get_cart_items(buyer):
        cart = CartService.get_cart(buyer)
        return cart.items.select_related('seller', 'variant')

    @staticmethod
    @transaction.atomic
    def add_to_cart(buyer, seller_id, variant_id, quantity=1, notes=''):
        cart = CartService.get_cart(buyer)

        try:
            pricing = SellerPricing.objects.get(
                seller_id=seller_id,
                variant_id=variant_id,
                is_active=True,
            )
        except SellerPricing.DoesNotExist:
            raise ValueError('Product not available from this seller')

        if quantity < pricing.minimum_order_quantity:
            raise ValueError(f'Minimum order quantity is {pricing.minimum_order_quantity}')

        inventory = Inventory.objects.filter(
            seller_id=seller_id,
            variant_id=variant_id,
        ).first()

        if inventory and inventory.available_stock < quantity:
            raise ValueError('Insufficient stock')

        unit_price = PricingService.get_price_for_quantity(pricing, quantity)

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            seller_id=seller_id,
            variant_id=variant_id,
            defaults={
                'quantity': quantity,
                'unit_price': unit_price,
                'tax_rate': pricing.tax_rate,
                'shipping_charge': pricing.shipping_charge,
                'notes': notes,
            },
        )

        if not created:
            cart_item.quantity += quantity
            cart_item.unit_price = PricingService.get_price_for_quantity(pricing, cart_item.quantity)
            cart_item.save()

        return cart_item

    @staticmethod
    def update_cart_item(cart_item_id, buyer, quantity):
        cart = CartService.get_cart(buyer)
        cart_item = CartItem.objects.get(id=cart_item_id, cart=cart)

        if quantity < 1:
            raise ValueError('Quantity must be at least 1')

        pricing = SellerPricing.objects.filter(
            seller=cart_item.seller,
            variant=cart_item.variant,
            is_active=True,
        ).first()

        if pricing and quantity < pricing.minimum_order_quantity:
            raise ValueError(f'Minimum order quantity is {pricing.minimum_order_quantity}')

        inventory = Inventory.objects.filter(
            seller=cart_item.seller,
            variant=cart_item.variant,
        ).first()

        if inventory and inventory.available_stock < quantity:
            raise ValueError('Insufficient stock')

        cart_item.quantity = quantity
        if pricing:
            cart_item.unit_price = PricingService.get_price_for_quantity(pricing, quantity)
        cart_item.save()
        return cart_item

    @staticmethod
    def remove_from_cart(cart_item_id, buyer):
        cart = CartService.get_cart(buyer)
        deleted, _ = CartItem.objects.filter(id=cart_item_id, cart=cart).delete()
        return deleted > 0

    @staticmethod
    def clear_cart(buyer):
        cart = CartService.get_cart(buyer)
        cart.items.all().delete()
        return True
