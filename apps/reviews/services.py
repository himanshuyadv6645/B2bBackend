from django.db.models import Avg
from apps.reviews.models import ProductReview, SellerReview
from apps.orders.models import OrderItem


class ReviewService:
    @staticmethod
    def update_product_rating(product):
        avg_rating = ProductReview.objects.filter(
            product=product, is_active=True, status='approved'
        ).aggregate(avg=Avg('rating'))['avg'] or 0
        product.average_rating = round(avg_rating, 2)
        product.total_reviews = ProductReview.objects.filter(
            product=product, is_active=True, status='approved'
        ).count()
        product.save(update_fields=['average_rating', 'total_reviews', 'updated_at'])

    @staticmethod
    def update_seller_rating(seller):
        avg_rating = SellerReview.objects.filter(
            seller=seller, is_active=True, status='approved'
        ).aggregate(avg=Avg('rating'))['avg'] or 0
        seller.rating = round(avg_rating, 2)
        seller.total_ratings = SellerReview.objects.filter(
            seller=seller, is_active=True, status='approved'
        ).count()
        seller.save(update_fields=['rating', 'total_ratings', 'updated_at'])

    @staticmethod
    def create_product_review(buyer, data):
        try:
            order_item = OrderItem.objects.get(
                id=data['order_item_id'],
                order__buyer=buyer,
                order__status='delivered',
            )
        except OrderItem.DoesNotExist:
            raise ValueError('You can only review products from delivered orders')

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
            status='pending',
        )
        return review

    @staticmethod
    def get_product_reviews(product_id):
        return ProductReview.objects.filter(
            product_id=product_id, is_active=True, status='approved'
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
                status='pending',
            )
            reviews.append(review)

        return reviews

    @staticmethod
    def get_seller_reviews(seller_id):
        return SellerReview.objects.filter(
            seller_id=seller_id, is_active=True, status='approved'
        ).select_related('buyer')

    @staticmethod
    def approve_product_review(review_id):
        review = ProductReview.objects.get(id=review_id)
        review.status = 'approved'
        review.save(update_fields=['status'])
        ReviewService.update_product_rating(review.product)
        return review

    @staticmethod
    def reject_product_review(review_id):
        review = ProductReview.objects.get(id=review_id)
        review.status = 'rejected'
        review.save(update_fields=['status'])
        ReviewService.update_product_rating(review.product)
        return review

    @staticmethod
    def approve_seller_review(review_id):
        review = SellerReview.objects.get(id=review_id)
        review.status = 'approved'
        review.save(update_fields=['status'])
        ReviewService.update_seller_rating(review.seller)
        return review

    @staticmethod
    def reject_seller_review(review_id):
        review = SellerReview.objects.get(id=review_id)
        review.status = 'rejected'
        review.save(update_fields=['status'])
        ReviewService.update_seller_rating(review.seller)
        return review
