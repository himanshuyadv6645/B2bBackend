from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'level', 'sort_order', 'is_active')
    list_filter = ('is_active', 'level')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
