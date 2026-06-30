from rest_framework import serializers
from apps.brands.models import Brand


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = [
            'id', 'name', 'slug', 'logo', 'description', 'website',
            'is_active', 'is_featured', 'sort_order', 'created_at',
        ]


class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name', 'slug', 'logo', 'is_featured']
