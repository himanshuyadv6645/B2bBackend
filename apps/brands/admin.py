from django.contrib import admin
from .models import Brand


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'is_featured', 'sort_order')
    list_filter = ('is_active', 'is_featured')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
