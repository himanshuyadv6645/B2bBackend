from django.urls import path
from apps.products.views.product import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
)
from apps.products.views.image import (
    ProductImageListCreateView,
    ProductImageDeleteView,
)

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),
    path('create/', ProductCreateView.as_view(), name='product-create'),
    path('<uuid:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('<uuid:product_pk>/images/', ProductImageListCreateView.as_view(), name='product-images'),
    path('<uuid:product_pk>/images/<uuid:pk>/delete/', ProductImageDeleteView.as_view(), name='product-image-delete'),
]
