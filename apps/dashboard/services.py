from django.db.models import Sum, Count, Avg
from django.utils import timezone
from datetime import timedelta
from apps.orders.models import Order, OrderItem
from apps.products.models import Product
from apps.reviews.models import ProductReview, SellerReview


class DashboardService:
    @staticmethod
    def get_buyer_dashboard(buyer):
        from apps.wishlist.models import Wishlist
        from apps.cart.models import Cart

        order_stats = Order.objects.filter(buyer=buyer).aggregate(
            total_orders=Count('id'),
            total_spent=Sum('total_amount'),
        )

        recent_orders = Order.objects.filter(buyer=buyer)[:5]
        wishlist_count = Wishlist.objects.filter(buyer=buyer).count()

        try:
            cart = Cart.objects.get(buyer=buyer)
            cart_count = cart.items.count()
        except Cart.DoesNotExist:
            cart_count = 0

        return {
            'total_orders': order_stats['total_orders'] or 0,
            'total_spent': float(order_stats['total_spent'] or 0),
            'recent_orders': recent_orders,
            'wishlist_count': wishlist_count,
            'cart_count': cart_count,
        }

    @staticmethod
    def get_seller_dashboard(seller):
        order_stats = OrderItem.objects.filter(seller=seller).aggregate(
            total_orders=Count('id'),
            total_revenue=Sum('total_price'),
        )

        recent_orders = OrderItem.objects.filter(seller=seller).select_related('order')[:5]
        product_count = Product.objects.filter(
            variants__seller_pricing__seller=seller,
            deleted_at__isnull=True,
        ).distinct().count()

        return {
            'total_orders': order_stats['total_orders'] or 0,
            'total_revenue': float(order_stats['total_revenue'] or 0),
            'recent_orders': recent_orders,
            'product_count': product_count,
        }

    @staticmethod
    def get_admin_dashboard():
        from apps.authentication.models import User
        from apps.sellers.models import SellerProfile

        stats = {
            'total_users': User.objects.count(),
            'total_buyers': User.objects.filter(role='buyer').count(),
            'total_sellers': User.objects.filter(role='seller').count(),
            'pending_sellers': SellerProfile.objects.filter(status='pending').count(),
            'total_orders': Order.objects.count(),
            'total_revenue': float(Order.objects.filter(payment_status='paid').aggregate(total=Sum('total_amount'))['total'] or 0),
            'total_products': Product.objects.filter(deleted_at__isnull=True).count(),
        }

        recent_orders = Order.objects.all()[:10]
        stats['recent_orders'] = recent_orders

        return stats
