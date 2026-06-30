from django.urls import path
from apps.product_variants.views.variant import (
    ProductVariantListView,
    ProductVariantDetailView,
    ProductVariantCreateView,
    ProductVariantUpdateView,
)
from apps.product_variants.views.image import (
    VariantImageListCreateView,
    VariantImageDeleteView,
)

app_name = 'product_variants'

urlpatterns = [
    path('', ProductVariantListView.as_view(), name='variant-list'),
    path('<uuid:pk>/', ProductVariantDetailView.as_view(), name='variant-detail'),
    path('create/', ProductVariantCreateView.as_view(), name='variant-create'),
    path('<uuid:pk>/update/', ProductVariantUpdateView.as_view(), name='variant-update'),
    path('<uuid:variant_pk>/images/', VariantImageListCreateView.as_view(), name='variant-images'),
    path('<uuid:variant_pk>/images/<uuid:pk>/delete/', VariantImageDeleteView.as_view(), name='variant-image-delete'),
]
