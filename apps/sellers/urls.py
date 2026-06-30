from django.urls import path
from apps.sellers.views.seller import (
    SellerProfileView,
    SellerWarehouseListCreateView,
    SellerWarehouseDetailView,
    AdminSellerListView,
    AdminSellerApproveView,
)

app_name = 'sellers'

urlpatterns = [
    path('profile/', SellerProfileView.as_view(), name='seller-profile'),
    path('warehouses/', SellerWarehouseListCreateView.as_view(), name='seller-warehouses'),
    path('warehouses/<uuid:pk>/', SellerWarehouseDetailView.as_view(), name='seller-warehouse-detail'),
    path('admin/sellers/', AdminSellerListView.as_view(), name='admin-seller-list'),
    path('admin/sellers/<uuid:pk>/approve/', AdminSellerApproveView.as_view(), name='admin-seller-approve'),
]
