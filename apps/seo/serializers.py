from rest_framework import serializers
from .models import SEOPage, SEOFAQ


class SEOFAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = SEOFAQ
        fields = ['id', 'question', 'answer', 'sort_order']


class SEOPageListSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True, default='')
    category_slug = serializers.CharField(source='category.slug', read_only=True, default='')
    brand_name = serializers.CharField(source='brand.name', read_only=True, default='')
    brand_slug = serializers.CharField(source='brand.slug', read_only=True, default='')

    class Meta:
        model = SEOPage
        fields = [
            'id', 'page_type', 'slug', 'title', 'h1_heading',
            'city', 'state', 'category_name', 'category_slug',
            'brand_name', 'brand_slug', 'meta_description',
        ]


class SEOPageDetailSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True, default='')
    category_slug = serializers.CharField(source='category.slug', read_only=True, default='')
    category_image = serializers.CharField(source='category.image', read_only=True, default='')
    brand_name = serializers.CharField(source='brand.name', read_only=True, default='')
    brand_slug = serializers.CharField(source='brand.slug', read_only=True, default='')
    brand_logo = serializers.CharField(source='brand.logo', read_only=True, default='')
    faqs = SEOFAQSerializer(many=True, read_only=True)

    class Meta:
        model = SEOPage
        fields = [
            'id', 'page_type', 'slug', 'title', 'h1_heading',
            'meta_description', 'meta_keywords',
            'city', 'state', 'country',
            'intro_text', 'buying_guide', 'why_choose_us',
            'faq_json', 'related_searches',
            'canonical_url', 'og_title', 'og_description', 'og_image',
            'schema_json', 'views_count',
            'category_name', 'category_slug', 'category_image',
            'brand_name', 'brand_slug', 'brand_logo',
            'faqs',
        ]
