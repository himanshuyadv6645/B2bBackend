from django.urls import path
from apps.brands.views.brand import (
    BrandListView,
    BrandDetailView,
    AdminBrandCreateView,
)

app_name = 'brands'

urlpatterns = [
    path('', BrandListView.as_view(), name='brand-list'),
    path('<slug:slug>/', BrandDetailView.as_view(), name='brand-detail'),
    path('admin/create/', AdminBrandCreateView.as_view(), name='admin-brand-create'),
]
