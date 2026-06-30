from rest_framework import serializers
from apps.products.models import Product, ProductAttribute, ProductImage, ProductDocument


class ProductAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttribute
        fields = ['id', 'key', 'value', 'sort_order']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image_url', 'alt_text', 'sort_order', 'is_primary']


class ProductDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDocument
        fields = ['id', 'title', 'file_url', 'file_type', 'file_size', 'sort_order']


class ProductListSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    brand_name = serializers.CharField(source='brand.name', read_only=True, default=None)
    primary_image = serializers.SerializerMethodField()
    discount_percent = serializers.IntegerField(read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'sku', 'category', 'category_name',
            'brand', 'brand_name', 'short_description',
            'retail_price', 'wholesale_price', 'min_selling_price', 'max_selling_price',
            'gst', 'moq', 'warranty', 'country_of_origin',
            'total_sellers', 'total_stock',
            'average_rating', 'total_reviews',
            'is_active', 'is_featured', 'is_trending', 'is_top_seller',
            'primary_image', 'discount_percent', 'created_at',
        ]

    def get_primary_image(self, obj):
        from common.serializer_helpers import get_product_image
        return get_product_image(obj)


class ProductDetailSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    brand_name = serializers.CharField(source='brand.name', read_only=True, default=None)
    attributes = ProductAttributeSerializer(many=True, read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)
    documents = ProductDocumentSerializer(many=True, read_only=True)
    variants = serializers.SerializerMethodField()
    primary_image = serializers.SerializerMethodField()
    discount_percent = serializers.IntegerField(read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'description', 'short_description', 'sku',
            'hsn_code', 'taxable', 'category', 'category_name', 'brand',
            'brand_name', 'is_active', 'is_featured', 'is_trending', 'is_top_seller',
            'is_digital', 'meta_title', 'meta_description', 'meta_keywords',
            'retail_price', 'wholesale_price', 'min_selling_price', 'max_selling_price',
            'gst', 'moq', 'warranty', 'country_of_origin',
            'weight', 'length', 'width', 'height', 'specifications',
            'total_sellers', 'total_stock', 'average_rating', 'total_reviews', 'views_count',
            'attributes', 'images', 'documents', 'variants', 'primary_image', 'discount_percent',
            'created_at', 'updated_at',
        ]

    def get_primary_image(self, obj):
        from common.serializer_helpers import get_product_image
        return get_product_image(obj)

    def get_variants(self, obj):
        from common.serializer_helpers import get_variant_image
        variants = []
        for v in obj.variants.filter(is_active=True):
            selling_price = getattr(v, 'min_selling_price', None)
            variants.append({
                'id': str(v.id),
                'name': v.name,
                'sku': v.sku,
                'slug': v.slug,
                'selling_price': str(selling_price) if selling_price is not None else None,
                'image': get_variant_image(v),
                'is_default': getattr(v, 'is_default', False),
            })
        return variants


class ProductCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name', 'description', 'short_description', 'category', 'brand',
            'sku', 'hsn_code', 'taxable', 'is_active', 'is_featured',
            'is_trending', 'is_top_seller',
            'retail_price', 'wholesale_price', 'gst', 'moq',
            'warranty', 'country_of_origin',
            'weight', 'length', 'width', 'height',
            'specifications',
            'meta_title', 'meta_description', 'meta_keywords',
        ]
