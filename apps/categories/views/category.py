from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema

from apps.categories.models import Category
from apps.categories.serializers.category import (
    CategoryListSerializer,
    CategoryDetailSerializer,
    CategoryTreeSerializer,
    CategoryCreateSerializer,
)
from common.permissions import IsAdminOrReadOnly
from common.response import success_response, created_response, not_found_response, bad_request_response
from common.pagination import StandardResultsPagination


class CategoryListView(generics.ListAPIView):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategoryListSerializer
    pagination_class = StandardResultsPagination

    def get_queryset(self):
        queryset = Category.objects.filter(
            is_active=True,
            deleted_at__isnull=True,
        ).select_related('parent')
        # Filter by parent (root categories by default)
        parent = self.request.query_params.get('parent')
        if parent == 'null' or parent == 'root':
            queryset = queryset.filter(parent__isnull=True)
        elif parent:
            queryset = queryset.filter(parent_id=parent)
        else:
            # Default: only root categories
            queryset = queryset.filter(parent__isnull=True)

        # Search
        search = self.request.query_params.get('search')
        if search:
            queryset = queryset.filter(name__icontains=search)

        # Featured filter
        is_featured = self.request.query_params.get('is_featured')
        if is_featured == 'true':
            queryset = queryset.filter(is_featured=True)

        return queryset

    @extend_schema(tags=['Categories'], summary='List categories')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategoryDetailSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return Category.objects.filter(deleted_at__isnull=True)

    @extend_schema(tags=['Categories'], summary='Get category with children')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(tags=['Categories'], summary='Update category')
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(tags=['Categories'], summary='Delete category (soft delete)')
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.soft_delete()
        return success_response(message='Category deleted')


class CategoryTreeView(generics.GenericAPIView):
    permission_classes = [IsAdminOrReadOnly]

    @extend_schema(tags=['Categories'], summary='Get full category tree')
    def get(self, request):
        from django.db.models import Count
        from apps.products.models import Product

        # Fetch ALL active categories in ONE query, build tree in Python
        all_cats = list(
            Category.objects.filter(
                is_active=True,
                deleted_at__isnull=True,
            ).order_by('sort_order', 'name')
        )

        # Pre-compute direct product counts per category
        cat_ids = [c.id for c in all_cats]
        product_counts = dict(
            Product.objects.filter(
                category_id__in=cat_ids, is_active=True, deleted_at__isnull=True
            ).values('category_id').annotate(cnt=Count('id')).values_list('category_id', 'cnt')
        )

        # Build lookup and tree structure
        cat_map = {}
        for cat in all_cats:
            cat_map[cat.id] = {
                'id': str(cat.id),
                'name': cat.name,
                'slug': cat.slug,
                'level': cat.level,
                'image': cat.image or '',
                'icon': cat.icon or '',
                'is_featured': cat.is_featured,
                'product_count': product_counts.get(cat.id, 0),
                'children': [],
            }

        roots = []
        for cat in all_cats:
            node = cat_map[cat.id]
            if cat.parent_id and cat.parent_id in cat_map:
                cat_map[cat.parent_id]['children'].append(node)
            elif cat.parent_id is None:
                roots.append(node)

        # Roll up product counts: parent counts include children
        def rollup_counts(node):
            total = node['product_count']
            for child in node['children']:
                total += rollup_counts(child)
            node['product_count'] = total
            return total

        for root in roots:
            rollup_counts(root)

        return success_response(data=roots)


class CategoryFeaturedView(generics.ListAPIView):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategoryListSerializer

    def get_queryset(self):
        return Category.objects.filter(
            is_featured=True,
            is_active=True,
            parent__isnull=True,
            deleted_at__isnull=True,
        )

    @extend_schema(tags=['Categories'], summary='Get featured categories')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CategorySearchView(generics.ListAPIView):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategoryListSerializer
    pagination_class = StandardResultsPagination

    def get_queryset(self):
        search = self.request.query_params.get('q', '')
        if not search:
            return Category.objects.none()
        return Category.objects.filter(
            name__icontains=search,
            is_active=True,
            deleted_at__isnull=True,
        )

    @extend_schema(tags=['Categories'], summary='Search categories by name')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CategoryAdminListView(generics.ListAPIView):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategoryListSerializer
    pagination_class = StandardResultsPagination

    def get_queryset(self):
        queryset = Category.objects.filter(deleted_at__isnull=True)
        parent = self.request.query_params.get('parent')
        if parent == 'null' or parent == 'root':
            queryset = queryset.filter(parent__isnull=True)
        elif parent:
            queryset = queryset.filter(parent_id=parent)
        else:
            queryset = queryset.filter(parent__isnull=True)
        return queryset

    @extend_schema(tags=['Categories'], summary='Admin: List all categories')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class AdminCategoryCreateView(generics.CreateAPIView):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategoryCreateSerializer

    @extend_schema(tags=['Categories'], summary='Admin: Create category')
    def post(self, request, *args, **kwargs):
        serializer = CategoryCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        category = serializer.save()
        return created_response(
            data=CategoryDetailSerializer(category).data,
            message='Category created',
        )


class AdminCategoryUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategoryCreateSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return Category.objects.filter(deleted_at__isnull=True)

    @extend_schema(tags=['Categories'], summary='Admin: Update category')
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(tags=['Categories'], summary='Admin: Update category')
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)


class AdminCategoryDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAdminOrReadOnly]
    lookup_field = 'pk'

    def get_queryset(self):
        return Category.objects.filter(deleted_at__isnull=True)

    @extend_schema(tags=['Categories'], summary='Admin: Delete category (soft delete)')
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.soft_delete()
        return success_response(message='Category deleted')


class AdminCategoryBulkStatusView(APIView):
    permission_classes = [IsAdminOrReadOnly]

    @extend_schema(tags=['Categories'], summary='Admin: Toggle category active status')
    def post(self, request):
        category_id = request.data.get('id')
        is_active = request.data.get('is_active')
        if not category_id:
            return bad_request_response(message='Category ID is required')
        try:
            category = Category.objects.get(id=category_id, deleted_at__isnull=True)
        except Category.DoesNotExist:
            return not_found_response('Category not found')
        if is_active is not None:
            category.is_active = is_active
            category.save(update_fields=['is_active'])
        return success_response(
            data=CategoryDetailSerializer(category).data,
            message='Category updated',
        )
