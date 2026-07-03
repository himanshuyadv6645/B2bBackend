from django.urls import path
from apps.reviews.views.review import (
    ProductReviewListCreateView,
    SellerReviewListCreateView,
)
from apps.reviews.views.admin import (
    AdminProductReviewListView,
    AdminApproveProductReviewView,
    AdminRejectProductReviewView,
    AdminSellerReviewListView,
    AdminApproveSellerReviewView,
    AdminRejectSellerReviewView,
)

app_name = 'reviews'

urlpatterns = [
    # Buyer endpoints
    path('products/', ProductReviewListCreateView.as_view(), name='product-reviews'),
    path('sellers/', SellerReviewListCreateView.as_view(), name='seller-reviews'),

    # Admin endpoints
    path('admin/products/', AdminProductReviewListView.as_view(), name='admin-product-reviews'),
    path('admin/products/<uuid:pk>/approve/', AdminApproveProductReviewView.as_view(), name='admin-approve-product-review'),
    path('admin/products/<uuid:pk>/reject/', AdminRejectProductReviewView.as_view(), name='admin-reject-product-review'),
    
    path('admin/sellers/', AdminSellerReviewListView.as_view(), name='admin-seller-reviews'),
    path('admin/sellers/<uuid:pk>/approve/', AdminApproveSellerReviewView.as_view(), name='admin-approve-seller-review'),
    path('admin/sellers/<uuid:pk>/reject/', AdminRejectSellerReviewView.as_view(), name='admin-reject-seller-review'),
]
