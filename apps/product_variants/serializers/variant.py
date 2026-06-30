from rest_framework import serializers
from apps.product_variants.models import ProductVariant, VariantAttribute, VariantImage


class VariantAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VariantAttribute
        fields = ['id', 'attribute_name', 'attribute_value']


class VariantImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = VariantImage
        fields = ['id', 'image_url', 'alt_text', 'sort_order', 'is_primary']


class ProductVariantListSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = ProductVariant
        fields = [
            'id', 'product', 'product_name', 'sku', 'name', 'slug',
            'is_active', 'min_selling_price', 'max_selling_price',
            'total_sellers', 'total_stock', 'average_rating', 'sort_order',
        ]


class ProductVariantDetailSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    attributes = VariantAttributeSerializer(many=True, read_only=True)
    images = VariantImageSerializer(many=True, read_only=True)

    class Meta:
        model = ProductVariant
        fields = [
            'id', 'product', 'product_name', 'sku', 'name', 'slug',
            'description', 'is_active', 'sort_order',
            'min_selling_price', 'max_selling_price',
            'total_sellers', 'total_stock', 'average_rating',
            'attributes', 'images',
            'created_at', 'updated_at',
        ]


class ProductVariantCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = ['product', 'sku', 'name', 'description', 'is_active', 'sort_order']
