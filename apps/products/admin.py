from django.contrib import admin
from .models import Product, ProductAttribute, ProductImage, ProductDocument


class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute
    extra = 0


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


class ProductDocumentInline(admin.TabularInline):
    model = ProductDocument
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'category', 'brand', 'is_active', 'is_featured', 'total_sellers', 'total_stock')
    list_filter = ('is_active', 'is_featured', 'category', 'brand')
    search_fields = ('name', 'sku')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductAttributeInline, ProductImageInline, ProductDocumentInline]


@admin.register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('product', 'key', 'value', 'sort_order')


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image_url', 'sort_order', 'is_primary')


@admin.register(ProductDocument)
class ProductDocumentAdmin(admin.ModelAdmin):
    list_display = ('product', 'title', 'file_type', 'file_size')
