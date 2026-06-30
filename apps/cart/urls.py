from django.urls import path
from apps.cart.views.cart import (
    CartView,
    AddToCartView,
    UpdateCartItemView,
    RemoveFromCartView,
    ClearCartView,
)

app_name = 'cart'

urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('add/', AddToCartView.as_view(), name='add-to-cart'),
    path('item/<uuid:item_id>/', UpdateCartItemView.as_view(), name='update-cart-item'),
    path('item/<uuid:item_id>/remove/', RemoveFromCartView.as_view(), name='remove-from-cart'),
    path('clear/', ClearCartView.as_view(), name='clear-cart'),
]
