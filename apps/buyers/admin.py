from django.contrib import admin
from .models import BuyerProfile, BuyerAddress


class BuyerAddressInline(admin.TabularInline):
    model = BuyerAddress
    extra = 0


@admin.register(BuyerProfile)
class BuyerProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'user', 'company_name', 'gstin', 'is_verified')
    list_filter = ('is_verified', 'business_type')
    search_fields = ('first_name', 'last_name', 'gstin', 'user__email')
    inlines = [BuyerAddressInline]


@admin.register(BuyerAddress)
class BuyerAddressAdmin(admin.ModelAdmin):
    list_display = ('buyer', 'address_type', 'city', 'state', 'pincode', 'is_default')
    list_filter = ('address_type', 'is_default')
