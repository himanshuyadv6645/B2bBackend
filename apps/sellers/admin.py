from django.contrib import admin
from .models import SellerProfile, SellerWarehouse


class SellerWarehouseInline(admin.TabularInline):
    model = SellerWarehouse
    extra = 0


@admin.register(SellerProfile)
class SellerProfileAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'gstin', 'status', 'rating', 'is_verified', 'created_at')
    list_filter = ('status', 'is_verified')
    search_fields = ('company_name', 'gstin', 'user__email')
    inlines = [SellerWarehouseInline]


@admin.register(SellerWarehouse)
class SellerWarehouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'seller', 'city', 'state', 'pincode', 'is_active', 'is_primary')
    list_filter = ('is_active', 'is_primary')
