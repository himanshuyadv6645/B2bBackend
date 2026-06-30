import uuid

from rest_framework import generics
from drf_spectacular.utils import extend_schema
from django.db.models import Q

from apps.products.models import Product
from apps.products.serializers.product import (
    ProductListSerializer,
    ProductDetailSerializer,
    ProductCreateUpdateSerializer,
)
from common.permissions import IsAdminOrReadOnly, IsSellerUser, IsApprovedSeller, IsAdminOrApprovedSeller
from common.response import success_response, created_response
from common.pagination import StandardResultsPagination


def _get_category_and_descendant_ids(category_value):
    """Resolve a category value (UUID or slug) to a set of category IDs
    including all descendants. Returns None if no match found."""
    from apps.categories.models import Category

    cat = None
    try:
        uuid.UUID(str(category_value))
        cat = Category.objects.filter(
            id=category_value, is_active=True, deleted_at__isnull=True
        ).first()
    except (ValueError, TypeError):
        cat = Category.objects.filter(
            slug=category_value, is_active=True, deleted_at__isnull=True
        ).first()

    if not cat:
        return None

    ids = {cat.id}
    queue = list(cat.children.filter(is_active=True, deleted_at__isnull=True))
    while queue:
        child = queue.pop()
        ids.add(child.id)
        queue.extend(child.children.filter(is_active=True, deleted_at__isnull=True))
    return ids


class ProductListView(generics.ListAPIView):
    permission_classes = []
    serializer_class = ProductListSerializer
    pagination_class = StandardResultsPagination

    def get_queryset(self):
        queryset = Product.objects.filter(
            is_active=True, deleted_at__isnull=True
        ).select_related('category', 'brand').prefetch_related('images')

        category = self.request.query_params.get('category')
        brand = self.request.query_params.get('brand')
        seller = self.request.query_params.get('seller')
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
        search = self.request.query_params.get('search')
        is_featured = self.request.query_params.get('is_featured')
        is_trending = self.request.query_params.get('is_trending')
        is_top_seller = self.request.query_params.get('is_top_seller')
        min_rating = self.request.query_params.get('min_rating')
        min_moq = self.request.query_params.get('min_moq')
        max_moq = self.request.query_params.get('max_moq')
        country = self.request.query_params.get('country')
        ordering = self.request.query_params.get('ordering', '-created_at')

        if category:
            cat_ids = _get_category_and_descendant_ids(category)
            if cat_ids is not None:
                queryset = queryset.filter(category_id__in=cat_ids)
            else:
                queryset = queryset.none()
        if brand:
            queryset = queryset.filter(brand_id=brand)
        if seller:
            queryset = queryset.filter(seller_id=seller)
        if min_price:
            queryset = queryset.filter(min_selling_price__gte=min_price)
        if max_price:
            queryset = queryset.filter(min_selling_price__lte=max_price)
        if search:
            from apps.categories.models import Category
            # Direct name match
            name_q = Q(name__icontains=search)
            # Also match products whose category keywords contain the search term
            matching_cats = Category.objects.filter(
                Q(keywords__icontains=search) | Q(name__icontains=search),
                is_active=True,
            )
            cat_ids = list(matching_cats.values_list('id', flat=True))
            if cat_ids:
                queryset = queryset.filter(
                    name_q | Q(category_id__in=cat_ids)
                )
            else:
                queryset = queryset.filter(name_q)
        if is_featured:
            queryset = queryset.filter(is_featured=True)
        if is_trending:
            queryset = queryset.filter(is_trending=True)
        if is_top_seller:
            queryset = queryset.filter(is_top_seller=True)
        if min_rating:
            queryset = queryset.filter(average_rating__gte=min_rating)
        if min_moq:
            queryset = queryset.filter(moq__lte=min_moq)
        if max_moq:
            queryset = queryset.filter(moq__gte=max_moq)
        if country:
            queryset = queryset.filter(country_of_origin__icontains=country)

        if ordering in [
            'name', '-name', 'min_selling_price', '-min_selling_price',
            'average_rating', '-average_rating', 'total_reviews', '-total_reviews',
            'created_at', '-created_at', 'total_stock', '-total_stock',
            'moq', '-moq',
        ]:
            queryset = queryset.order_by(ordering)

        return queryset

    @extend_schema(tags=['Products'], summary='List products with filters')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ProductDetailView(generics.RetrieveAPIView):
    permission_classes = []
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.filter(
        is_active=True, deleted_at__isnull=True
    ).select_related('category', 'brand').prefetch_related(
        'images', 'attributes', 'documents', 'variants', 'variants__images',
    )
    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs):
        from django.db.models import F
        instance = self.get_object()
        Product.objects.filter(id=instance.id).update(views_count=F('views_count') + 1)
        instance.refresh_from_db()
        serializer = self.get_serializer(instance)
        return success_response(data=serializer.data)

    @extend_schema(tags=['Products'], summary='Get product details')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ProductCreateView(generics.CreateAPIView):
    permission_classes = [IsAdminOrApprovedSeller]
    serializer_class = ProductCreateUpdateSerializer

    @extend_schema(tags=['Products'], summary='Create product (admin or seller)')
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ProductUpdateView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrApprovedSeller]
    serializer_class = ProductCreateUpdateSerializer
    queryset = Product.all_objects.all()

    @extend_schema(tags=['Products'], summary='Seller: Update product')
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(tags=['Products'], summary='Seller: Delete product (soft delete)')
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.soft_delete()
        return success_response(message='Product deleted')
