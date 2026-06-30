from django.contrib import admin
from .models import ProductReview, SellerReview


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'buyer', 'rating', 'is_verified', 'is_active', 'created_at')
    list_filter = ('rating', 'is_verified', 'is_active')


@admin.register(SellerReview)
class SellerReviewAdmin(admin.ModelAdmin):
    list_display = ('seller', 'buyer', 'order', 'rating', 'is_verified', 'is_active')
    list_filter = ('rating', 'is_verified', 'is_active')
