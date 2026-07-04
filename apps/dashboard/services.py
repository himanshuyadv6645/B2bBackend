from django.db.models import Sum, Count, Avg, Q
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
            # Cancelled orders are not money spent — exclude them from the total.
            total_spent=Sum('total_amount', filter=~Q(status='cancelled')),
        )

        recent_orders = Order.objects.filter(buyer=buyer)[:5]
        wishlist_count = Wishlist.objects.filter(buyer=buyer).count()

        try:
            cart = Cart.objects.get(buyer=buyer)
            cart_count = cart.items.count()
        except Cart.DoesNotExist:
            cart_count = 0

        pending_orders = Order.objects.filter(buyer=buyer).exclude(
            status__in=['delivered', 'cancelled']
        ).count()

        return {
            'total_orders': order_stats['total_orders'] or 0,
            'total_spent': float(order_stats['total_spent'] or 0),
            'pending_orders': pending_orders,
            'recent_orders': recent_orders,
            'wishlist_count': wishlist_count,
            'cart_count': cart_count,
        }

    @staticmethod
    def get_seller_dashboard(seller):
        order_stats = SellerOrder.objects.filter(seller=seller).aggregate(
            total_orders=Count('id'),
            pending_orders=Count('id', filter=Q(status='pending')),
            total_revenue=Sum('total_amount', filter=~Q(status='cancelled')),
            pending_revenue=Sum('total_amount', filter=Q(status='pending')),
        )

        recent_orders = SellerOrder.objects.filter(seller=seller).select_related(
            'order', 'order__buyer__user'
        ).order_by('-created_at')[:5]

        products = Product.objects.filter(
            variants__seller_pricing__seller=seller,
            deleted_at__isnull=True,
        ).distinct()
        total_products = products.count()
        active_products = products.filter(is_active=True).count()

        total_customers = SellerOrder.objects.filter(seller=seller).values(
            'order__buyer'
        ).distinct().count()
        today = timezone.now().date()
        new_customers_today = OrderItem.objects.filter(
            seller=seller, order__created_at__date=today,
        ).values('order__buyer').distinct().count()

        return {
            'total_products': total_products,
            'active_products': active_products,
            'product_count': total_products,  # backward-compatible alias
            'total_orders': order_stats['total_orders'] or 0,
            'pending_orders': order_stats['pending_orders'] or 0,
            'total_revenue': float(order_stats['total_revenue'] or 0),
            'pending_revenue': float(order_stats['pending_revenue'] or 0),
            'total_customers': total_customers,
            'new_customers_today': new_customers_today,
            'recent_orders': recent_orders,
        }

    @staticmethod
    def get_admin_dashboard():
        from datetime import timedelta
        from django.db.models.functions import TruncDate
        from apps.authentication.models import User
        from apps.sellers.models import SellerProfile
        from apps.orders.models import SellerOrder

        today = timezone.now().date()
        pending_sellers = SellerProfile.objects.filter(status='pending').count()

        stats = {
            'total_users': User.objects.count(),
            'total_buyers': User.objects.filter(role='buyer').count(),
            'total_sellers': User.objects.filter(role='seller').count(),
            'pending_sellers': pending_sellers,
            'pending_seller_approvals': pending_sellers,  # name the frontend reads
            'total_orders': Order.objects.count(),
            'orders_today': Order.objects.filter(created_at__date=today).count(),
            'total_revenue': float(Order.objects.filter(payment_status='paid').aggregate(total=Sum('total_amount'))['total'] or 0),
            'revenue_today': float(Order.objects.filter(payment_status='paid', created_at__date=today).aggregate(total=Sum('total_amount'))['total'] or 0),
            'total_products': Product.objects.filter(deleted_at__isnull=True).count(),
            'active_products': Product.objects.filter(is_active=True, deleted_at__isnull=True).count(),
        }

        # Top sellers by revenue (excluding cancelled seller orders)
        top = (
            SellerOrder.objects.exclude(status='cancelled')
            .values('seller_id', 'seller__company_name')
            .annotate(total_revenue=Sum('total_amount'), total_orders=Count('id'))
            .order_by('-total_revenue')[:6]
        )
        stats['top_sellers'] = [
            {
                'id': str(t['seller_id']),
                'company_name': t['seller__company_name'],
                'total_orders': t['total_orders'],
                'total_revenue': float(t['total_revenue'] or 0),
            }
            for t in top
        ]

        # Revenue chart: last 14 days of paid revenue + order counts per day
        start = today - timedelta(days=13)
        daily = (
            Order.objects.filter(created_at__date__gte=start)
            .annotate(day=TruncDate('created_at'))
            .values('day')
            .annotate(
                revenue=Sum('total_amount', filter=Q(payment_status='paid')),
                orders=Count('id'),
            )
            .order_by('day')
        )
        stats['revenue_chart'] = [
            {
                'date': d['day'].isoformat(),
                'revenue': str(d['revenue'] or 0),
                'orders': d['orders'],
            }
            for d in daily
        ]

        stats['recent_orders'] = Order.objects.all()[:10]

        return stats
