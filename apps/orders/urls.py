from django.urls import path
from apps.orders.views.order import (
    BuyerOrderListCreateView,
    BuyerOrderDetailView,
    BuyerCancelOrderView,
    SellerOrderListView,
    SellerOrderDetailView,
    SellerShipOrderView,
    SellerDeliverOrderView,
    InvoiceListView,
    InvoiceDetailView,
)

app_name = 'orders'

urlpatterns = [
    # Buyer endpoints
    path('', BuyerOrderListCreateView.as_view(), name='buyer-orders'),
    path('<str:order_number>/cancel/', BuyerCancelOrderView.as_view(), name='buyer-cancel-order'),
    path('<str:order_number>/', BuyerOrderDetailView.as_view(), name='buyer-order-detail'),
    
    # Seller endpoints
    path('seller/', SellerOrderListView.as_view(), name='seller-orders'),
    path('seller/<uuid:pk>/', SellerOrderDetailView.as_view(), name='seller-order-detail'),
    path('seller/<uuid:pk>/ship/', SellerShipOrderView.as_view(), name='seller-ship-order'),
    path('seller/<uuid:pk>/deliver/', SellerDeliverOrderView.as_view(), name='seller-deliver-order'),
    
    # Invoice endpoints
    path('invoices/', InvoiceListView.as_view(), name='invoice-list'),
    path('invoices/<uuid:pk>/', InvoiceDetailView.as_view(), name='invoice-detail'),
]
