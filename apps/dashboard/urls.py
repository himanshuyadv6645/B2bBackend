from django.urls import path
from apps.dashboard.views.dashboard import (
    BuyerDashboardView,
    SellerDashboardView,
    AdminDashboardView,
)

app_name = 'dashboard'

urlpatterns = [
    path('buyer/', BuyerDashboardView.as_view(), name='buyer-dashboard'),
    path('seller/', SellerDashboardView.as_view(), name='seller-dashboard'),
    path('admin/', AdminDashboardView.as_view(), name='admin-dashboard'),
]
