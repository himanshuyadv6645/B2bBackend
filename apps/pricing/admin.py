from django.contrib import admin
from .models import SellerPricing


@admin.register(SellerPricing)
class SellerPricingAdmin(admin.ModelAdmin):
    list_display = ('seller', 'variant', 'selling_price', 'tax_rate', 'is_active')
    list_filter = ('is_active', 'seller')
    search_fields = ('seller__company_name', 'variant__name')
