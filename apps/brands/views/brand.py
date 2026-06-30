from rest_framework import generics
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from apps.brands.models import Brand
from apps.brands.serializers.brand import BrandSerializer, BrandListSerializer
from common.permissions import IsAdminOrReadOnly
from common.response import success_response


class BrandListView(generics.ListAPIView):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = BrandListSerializer
    queryset = Brand.objects.filter(is_active=True)
    search_fields = ['name']
    ordering_fields = ['name', 'sort_order']

    @extend_schema(tags=['Brands'], summary='List all brands')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class BrandDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
    lookup_field = 'slug'

    @extend_schema(tags=['Brands'], summary='Get brand details')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class AdminBrandCreateView(generics.CreateAPIView):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = BrandSerializer

    @extend_schema(tags=['Brands'], summary='Admin: Create brand')
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
