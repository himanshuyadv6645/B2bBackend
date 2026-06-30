from rest_framework import generics
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from apps.product_variants.models import ProductVariant
from apps.product_variants.serializers.variant import (
    ProductVariantListSerializer,
    ProductVariantDetailSerializer,
    ProductVariantCreateSerializer,
)
from common.permissions import IsApprovedSeller
from common.pagination import StandardResultsPagination


class ProductVariantListView(generics.ListAPIView):
    permission_classes = []
    serializer_class = ProductVariantListSerializer
    pagination_class = StandardResultsPagination

    def get_queryset(self):
        queryset = ProductVariant.objects.filter(is_active=True, deleted_at__isnull=True)
        product_id = self.request.query_params.get('product')
        if product_id:
            queryset = queryset.filter(product_id=product_id)
        return queryset

    @extend_schema(tags=['Product Variants'], summary='List variants for a product')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ProductVariantDetailView(generics.RetrieveAPIView):
    permission_classes = []
    serializer_class = ProductVariantDetailSerializer
    queryset = ProductVariant.objects.filter(is_active=True, deleted_at__isnull=True)

    @extend_schema(tags=['Product Variants'], summary='Get variant details')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ProductVariantCreateView(generics.CreateAPIView):
    permission_classes = [IsApprovedSeller]
    serializer_class = ProductVariantCreateSerializer

    @extend_schema(tags=['Product Variants'], summary='Seller: Create variant')
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ProductVariantUpdateView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsApprovedSeller]
    serializer_class = ProductVariantCreateSerializer
    queryset = ProductVariant.objects.all()

    @extend_schema(tags=['Product Variants'], summary='Seller: Update variant')
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(tags=['Product Variants'], summary='Seller: Delete variant (soft delete)')
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.soft_delete()
        return Response({'success': True, 'message': 'Variant deleted'})
