from django.urls import path
from apps.inventory.views.inventory import (
    SellerInventoryListView,
    SellerInventoryCreateView,
    SellerStockAdjustView,
    SellerStockHistoryView,
)

app_name = 'inventory'

urlpatterns = [
    path('', SellerInventoryListView.as_view(), name='inventory-list'),
    path('create/', SellerInventoryCreateView.as_view(), name='inventory-create'),
    path('<uuid:pk>/adjust/', SellerStockAdjustView.as_view(), name='stock-adjust'),
    path('history/', SellerStockHistoryView.as_view(), name='stock-history'),
]
