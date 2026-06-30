from django.urls import path
from apps.pricing.views.pricing import (
    SellerPricingListView,
    SellerPricingCreateView,
    SellerPricingUpdateView,
    WholesaleTierListCreateView,
    WholesaleTierDeleteView,
    CompareSellersView,
)

app_name = 'pricing'

urlpatterns = [
    path('', SellerPricingListView.as_view(), name='pricing-list'),
    path('create/', SellerPricingCreateView.as_view(), name='pricing-create'),
    path('<uuid:pk>/', SellerPricingUpdateView.as_view(), name='pricing-detail'),
    path('<uuid:pricing_pk>/tiers/', WholesaleTierListCreateView.as_view(), name='wholesale-tier-list'),
    path('<uuid:pricing_pk>/tiers/<uuid:tier_pk>/', WholesaleTierDeleteView.as_view(), name='wholesale-tier-delete'),
    path('compare/<uuid:variant_id>/', CompareSellersView.as_view(), name='compare-sellers'),
]
