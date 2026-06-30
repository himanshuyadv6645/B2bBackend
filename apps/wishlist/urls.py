from django.urls import path
from apps.wishlist.views.wishlist import WishlistListCreateView, WishlistDeleteView

app_name = 'wishlist'

urlpatterns = [
    path('', WishlistListCreateView.as_view(), name='wishlist-list'),
    path('<uuid:pk>/', WishlistDeleteView.as_view(), name='wishlist-delete'),
]
