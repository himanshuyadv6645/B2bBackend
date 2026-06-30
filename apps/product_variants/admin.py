from django.contrib import admin
from .models import ProductVariant, VariantAttribute, VariantImage


class VariantAttributeInline(admin.TabularInline):
    model = VariantAttribute
    extra = 0


class VariantImageInline(admin.TabularInline):
    model = VariantImage
    extra = 0


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'sku', 'is_active', 'total_sellers', 'total_stock')
    list_filter = ('is_active', 'product')
    search_fields = ('name', 'sku')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [VariantAttributeInline, VariantImageInline]
