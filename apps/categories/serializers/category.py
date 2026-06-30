from rest_framework import serializers
from apps.categories.models import Category


class CategoryListSerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()
    children_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = [
            'id', 'name', 'slug', 'image', 'thumbnail', 'icon',
            'sort_order', 'level', 'is_active', 'is_featured',
            'product_count', 'children_count',
        ]

    def get_product_count(self, obj):
        from apps.products.models import Product
        return Product.objects.filter(
            category=obj,
            is_active=True,
            deleted_at__isnull=True,
        ).count()

    def get_children_count(self, obj):
        return obj.children.filter(is_active=True, deleted_at__isnull=True).count()


class CategoryDetailSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()
    product_count = serializers.SerializerMethodField()
    ancestors = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = [
            'id', 'parent', 'name', 'slug', 'description', 'image', 'thumbnail',
            'icon', 'sort_order', 'is_active', 'is_featured',
            'meta_title', 'meta_description',
            'level', 'path', 'children', 'product_count', 'ancestors',
            'created_at', 'updated_at',
        ]

    def get_children(self, obj):
        children = obj.children.filter(is_active=True, deleted_at__isnull=True)
        return CategoryListSerializer(children, many=True).data

    def get_product_count(self, obj):
        from apps.products.models import Product
        return Product.objects.filter(
            category=obj,
            is_active=True,
            deleted_at__isnull=True,
        ).count()

    def get_ancestors(self, obj):
        ancestors = obj.get_ancestors
        return CategoryListSerializer(ancestors, many=True).data


class CategoryTreeSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()
    product_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'level', 'image', 'icon', 'is_featured', 'product_count', 'children']

    def get_children(self, obj):
        if getattr(self, '_depth', 0) >= 2:
            return []
        children = obj.children.filter(is_active=True, deleted_at__isnull=True)
        self._depth = getattr(self, '_depth', 0) + 1
        result = CategoryTreeSerializer(children, many=True, context=self.context).data
        self._depth -= 1
        return result

    def get_product_count(self, obj):
        if not hasattr(self, '_product_counts'):
            self._product_counts = {}
        if obj.id not in self._product_counts:
            from apps.products.models import Product
            self._product_counts[obj.id] = Product.objects.filter(
                category=obj,
                is_active=True,
                deleted_at__isnull=True,
            ).count()
        return self._product_counts[obj.id]


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name', 'parent', 'description', 'image', 'thumbnail', 'icon',
            'sort_order', 'is_active', 'is_featured',
            'meta_title', 'meta_description',
        ]

    def validate_parent(self, value):
        if value and self.instance and value.id == self.instance.id:
            raise serializers.ValidationError('A category cannot be its own parent.')
        return value

    def validate_name(self, value):
        parent_id = self.initial_data.get('parent')
        parent = None
        if parent_id:
            try:
                parent = Category.objects.get(id=parent_id)
            except Category.DoesNotExist:
                pass
        queryset = Category.objects.filter(
            name=value,
            parent=parent,
            deleted_at__isnull=True,
        )
        if self.instance:
            queryset = queryset.exclude(id=self.instance.id)
        if queryset.exists():
            raise serializers.ValidationError('A category with this name already exists under the same parent.')
        return value
