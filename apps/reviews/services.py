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
        
        # Update ratings for individual variants
        for variant in product.variants.all():
            v_avg = ProductReview.objects.filter(
                variant=variant, is_active=True, status='approved'
            ).aggregate(avg=Avg('rating'))['avg'] or 0
            variant.average_rating = round(v_avg, 2)
            variant.save(update_fields=['average_rating'])

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
                status='delivered',
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
        from apps.orders.models import SellerOrder
        seller_id = data.get('seller_id')
        if not seller_id:
            raise ValueError('seller_id is required')
            
        try:
            seller_order = SellerOrder.objects.get(
                order_id=data['order_id'],
                seller_id=seller_id,
                order__buyer=buyer,
                status='delivered',
            )
        except SellerOrder.DoesNotExist:
            raise ValueError('Invalid order or this seller has not delivered their portion yet')

        if SellerReview.objects.filter(buyer=buyer, order_id=data['order_id'], seller_id=seller_id).exists():
            raise ValueError('You have already reviewed this seller for this order')

        review = SellerReview.objects.create(
            seller_id=seller_id,
            buyer=buyer,
            order_id=data['order_id'],
            rating=data['rating'],
            title=data.get('title', ''),
            comment=data.get('comment', ''),
            is_verified=True,
            status='pending',
        )

        return review

    @staticmethod
    def get_seller_reviews(seller_id):
        return SellerReview.objects.filter(
            seller_id=seller_id, is_active=True, status='approved'
        ).select_related('buyer')

    @staticmethod
    def approve_product_review(review_id):
        review = ProductReview.objects.get(id=review_id)
        review.status = 'approved'
        review.save(update_fields=['status', 'updated_at'])
        ReviewService.update_product_rating(review.product)
        return review

    @staticmethod
    def reject_product_review(review_id):
        review = ProductReview.objects.get(id=review_id)
        review.status = 'rejected'
        review.save(update_fields=['status', 'updated_at'])
        ReviewService.update_product_rating(review.product)
        return review

    @staticmethod
    def approve_seller_review(review_id):
        review = SellerReview.objects.get(id=review_id)
        review.status = 'approved'
        review.save(update_fields=['status', 'updated_at'])
        ReviewService.update_seller_rating(review.seller)
        return review

    @staticmethod
    def reject_seller_review(review_id):
        review = SellerReview.objects.get(id=review_id)
        review.status = 'rejected'
        review.save(update_fields=['status', 'updated_at'])
        ReviewService.update_seller_rating(review.seller)
        return review
