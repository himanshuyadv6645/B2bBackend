from django.db.models import Avg
from apps.reviews.models import ProductReview, SellerReview
from apps.orders.models import OrderItem


class ReviewService:
    @staticmethod
    def create_product_review(buyer, data):
        try:
            order_item = OrderItem.objects.get(
                id=data['order_item_id'],
                order__buyer=buyer,
            )
        except OrderItem.DoesNotExist:
            raise ValueError('Invalid order item')

        # Check if already reviewed
        if ProductReview.objects.filter(buyer=buyer, order_item=order_item).exists():
            raise ValueError('You have already reviewed this item')

        review = ProductReview.objects.create(
            product=order_item.variant.product,
            variant=order_item.variant,
            buyer=buyer,
            order_item=order_item,
            seller=order_item.seller,
            rating=data['rating'],
            title=data.get('title', ''),
            comment=data.get('comment', ''),
            is_verified=True,
        )

        # Update product rating
        product = order_item.variant.product
        avg_rating = ProductReview.objects.filter(
            product=product, is_active=True
        ).aggregate(avg=Avg('rating'))['avg'] or 0
        product.average_rating = round(avg_rating, 2)
        product.total_reviews = ProductReview.objects.filter(
            product=product, is_active=True
        ).count()
        product.save(update_fields=['average_rating', 'total_reviews', 'updated_at'])

        return review

    @staticmethod
    def get_product_reviews(product_id):
        return ProductReview.objects.filter(
            product_id=product_id, is_active=True
        ).select_related('buyer')

    @staticmethod
    def create_seller_review(buyer, data):
        from apps.orders.models import Order
        try:
            order = Order.objects.get(
                id=data['order_id'],
                buyer=buyer,
                status='delivered',
            )
        except Order.DoesNotExist:
            raise ValueError('Invalid order')

        if SellerReview.objects.filter(buyer=buyer, order=order).exists():
            raise ValueError('You have already reviewed this seller')

        # Create review for each seller in the order
        reviews = []
        for seller_order in order.seller_orders.all():
            review = SellerReview.objects.create(
                seller=seller_order.seller,
                buyer=buyer,
                order=order,
                rating=data['rating'],
                title=data.get('title', ''),
                comment=data.get('comment', ''),
                is_verified=True,
            )
            reviews.append(review)

            # Update seller rating
            seller = seller_order.seller
            avg_rating = SellerReview.objects.filter(
                seller=seller, is_active=True
            ).aggregate(avg=Avg('rating'))['avg'] or 0
            seller.rating = round(avg_rating, 2)
            seller.total_ratings = SellerReview.objects.filter(
                seller=seller, is_active=True
            ).count()
            seller.save(update_fields=['rating', 'total_ratings', 'updated_at'])

        return reviews

    @staticmethod
    def get_seller_reviews(seller_id):
        return SellerReview.objects.filter(
            seller_id=seller_id, is_active=True
        ).select_related('buyer')
