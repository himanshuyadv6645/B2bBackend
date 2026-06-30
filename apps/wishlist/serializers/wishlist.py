from rest_framework import serializers
from apps.wishlist.models import Wishlist


class WishlistSerializer(serializers.ModelSerializer):
    variant_name = serializers.CharField(source='variant.name', read_only=True)
    variant_slug = serializers.CharField(source='variant.slug', read_only=True)
    product_name = serializers.CharField(source='variant.product.name', read_only=True)
    variant_detail = serializers.SerializerMethodField()

    class Meta:
        model = Wishlist
        fields = ['id', 'variant', 'variant_name', 'variant_slug', 'product_name', 'variant_detail', 'created_at']
        read_only_fields = ['id', 'created_at']

    def get_variant_detail(self, obj):
        from common.serializer_helpers import build_variant_detail
        return build_variant_detail(obj.variant)
