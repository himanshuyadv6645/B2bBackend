from django.urls import path
from apps.reviews.views.review import (
    ProductReviewListCreateView,
    SellerReviewListCreateView,
)

app_name = 'reviews'

urlpatterns = [
    path('products/', ProductReviewListCreateView.as_view(), name='product-reviews'),
    path('sellers/', SellerReviewListCreateView.as_view(), name='seller-reviews'),
]
