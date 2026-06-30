from rest_framework import serializers
from apps.cart.models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):
    variant_name = serializers.CharField(source='variant.name', read_only=True)
    seller_name = serializers.CharField(source='seller.company_name', read_only=True)
    variant_detail = serializers.SerializerMethodField()
    variant_image = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = [
            'id', 'seller', 'seller_name', 'variant', 'variant_name', 'variant_detail', 'variant_image',
            'quantity', 'unit_price', 'tax_rate', 'shipping_charge',
            'total_price', 'notes', 'created_at',
        ]
        read_only_fields = ['id', 'total_price', 'created_at']

    def get_variant_detail(self, obj):
        from common.serializer_helpers import build_variant_detail
        return build_variant_detail(obj.variant)

    def get_variant_image(self, obj):
        from common.serializer_helpers import get_variant_image
        return get_variant_image(obj.variant)


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_items = serializers.ReadOnlyField()
    total_amount = serializers.ReadOnlyField()

    class Meta:
        model = Cart
        fields = ['id', 'items', 'total_items', 'total_amount', 'created_at', 'updated_at']


class AddToCartSerializer(serializers.Serializer):
    seller_id = serializers.UUIDField()
    variant_id = serializers.UUIDField()
    quantity = serializers.IntegerField(min_value=1, default=1)
    notes = serializers.CharField(max_length=500, required=False, allow_blank=True)


class UpdateCartItemSerializer(serializers.Serializer):
    quantity = serializers.IntegerField(min_value=1)
