from rest_framework import serializers
from apps.reviews.models import ProductReview, SellerReview


class ProductReviewSerializer(serializers.ModelSerializer):
    buyer_name = serializers.CharField(source='buyer.full_name', read_only=True)
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = ProductReview
        fields = [
            'id', 'product', 'product_name', 'variant', 'buyer', 'buyer_name', 'seller',
            'order_item', 'rating', 'title', 'comment', 'images',
            'is_verified', 'is_active', 'status', 'created_at',
        ]
        read_only_fields = ['id', 'buyer', 'is_verified', 'status', 'created_at']


class ProductReviewCreateSerializer(serializers.Serializer):
    order_item_id = serializers.UUIDField()
    variant_id = serializers.UUIDField(required=False, allow_null=True)
    rating = serializers.IntegerField(min_value=1, max_value=5)
    title = serializers.CharField(max_length=255, required=False, allow_blank=True)
    comment = serializers.CharField(required=False, allow_blank=True)


class SellerReviewSerializer(serializers.ModelSerializer):
    buyer_name = serializers.CharField(source='buyer.full_name', read_only=True)
    seller_name = serializers.CharField(source='seller.company_name', read_only=True)

    class Meta:
        model = SellerReview
        fields = [
            'id', 'seller', 'seller_name', 'buyer', 'buyer_name', 'order',
            'rating', 'title', 'comment', 'is_verified', 'is_active', 'status', 'created_at',
        ]
        read_only_fields = ['id', 'buyer', 'is_verified', 'status', 'created_at']
