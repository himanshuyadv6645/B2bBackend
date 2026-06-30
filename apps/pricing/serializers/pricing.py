from rest_framework import serializers
from apps.pricing.models import SellerPricing, WholesaleTier


class WholesaleTierSerializer(serializers.ModelSerializer):
    range_display = serializers.ReadOnlyField()

    class Meta:
        model = WholesaleTier
        fields = [
            'id', 'min_quantity', 'max_quantity', 'price_per_unit',
            'discount_percent', 'notes', 'range_display', 'created_at',
        ]
        read_only_fields = ['id', 'created_at']


class WholesaleTierCreateSerializer(serializers.Serializer):
    min_quantity = serializers.IntegerField(min_value=1)
    max_quantity = serializers.IntegerField(min_value=1, required=False, allow_null=True)
    price_per_unit = serializers.DecimalField(max_digits=12, decimal_places=2, min_value=0)
    discount_percent = serializers.DecimalField(max_digits=5, decimal_places=2, default=0, min_value=0)
    notes = serializers.CharField(max_length=200, required=False, allow_blank=True)

    def validate(self, data):
        if data.get('max_quantity') and data['min_quantity'] > data['max_quantity']:
            raise serializers.ValidationError('min_quantity cannot be greater than max_quantity')
        return data


class SellerPricingSerializer(serializers.ModelSerializer):
    variant_name = serializers.CharField(source='variant.name', read_only=True)
    seller_name = serializers.CharField(source='seller.company_name', read_only=True)
    variant_detail = serializers.SerializerMethodField()
    warehouse_detail = serializers.SerializerMethodField()
    wholesale_tiers = WholesaleTierSerializer(many=True, read_only=True)

    class Meta:
        model = SellerPricing
        fields = [
            'id', 'seller', 'seller_name', 'variant', 'variant_name', 'variant_detail',
            'warehouse', 'warehouse_detail', 'selling_price', 'offer_price',
            'discount_percent', 'tax_rate', 'tax_inclusive',
            'shipping_charge', 'free_shipping',
            'minimum_order_quantity', 'max_order_quantity',
            'warranty_type', 'warranty_period',
            'delivery_time_days', 'estimated_delivery',
            'wholesale_tiers',
            'is_active', 'valid_from', 'valid_till',
            'created_at', 'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_variant_detail(self, obj):
        from common.serializer_helpers import build_variant_detail
        return build_variant_detail(obj.variant)

    def get_warehouse_detail(self, obj):
        w = obj.warehouse
        if not w:
            return None
        return {'id': str(w.id), 'name': w.name, 'city': getattr(w, 'city', None)}


class SellerPricingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerPricing
        fields = [
            'variant', 'warehouse', 'selling_price', 'offer_price',
            'discount_percent', 'tax_rate', 'tax_inclusive',
            'shipping_charge', 'free_shipping',
            'minimum_order_quantity', 'max_order_quantity',
            'warranty_type', 'warranty_period',
            'delivery_time_days', 'estimated_delivery',
        ]


class BuyerPricingViewSerializer(serializers.ModelSerializer):
    variant_name = serializers.CharField(source='variant.name', read_only=True)
    seller_name = serializers.CharField(source='seller.company_name', read_only=True)
    seller_rating = serializers.DecimalField(source='seller.rating', max_digits=3, decimal_places=2, read_only=True)
    wholesale_tiers = WholesaleTierSerializer(many=True, read_only=True)
    effective_price = serializers.SerializerMethodField()

    class Meta:
        model = SellerPricing
        fields = [
            'id', 'seller', 'seller_name', 'seller_rating',
            'variant', 'variant_name',
            'selling_price', 'offer_price', 'discount_percent',
            'tax_rate', 'tax_inclusive',
            'shipping_charge', 'free_shipping',
            'minimum_order_quantity', 'max_order_quantity',
            'warranty_type', 'warranty_period',
            'delivery_time_days', 'estimated_delivery',
            'wholesale_tiers',
        ]

    def get_effective_price(self, obj):
        if obj.offer_price:
            return obj.offer_price
        return obj.selling_price
