from django.urls import path
from apps.buyers.views.buyer import (
    BuyerProfileView,
    BuyerAddressListCreateView,
    BuyerAddressDetailView,
    SaveDetectedLocationView,
)

app_name = 'buyers'

urlpatterns = [
    path('profile/', BuyerProfileView.as_view(), name='buyer-profile'),
    path('addresses/', BuyerAddressListCreateView.as_view(), name='buyer-addresses'),
    path('addresses/<uuid:pk>/', BuyerAddressDetailView.as_view(), name='buyer-address-detail'),
    path('locations/detect/', SaveDetectedLocationView.as_view(), name='save-detected-location'),
]
