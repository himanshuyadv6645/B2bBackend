from django.contrib import admin
from .models import Inventory, StockHistory, InventoryLog


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('seller', 'variant', 'warehouse', 'total_stock', 'reserved_stock', 'available_stock')
    list_filter = ('seller',)


@admin.register(StockHistory)
class StockHistoryAdmin(admin.ModelAdmin):
    list_display = ('inventory', 'change_type', 'quantity_change', 'previous_stock', 'new_stock', 'created_at')
    list_filter = ('change_type',)


@admin.register(InventoryLog)
class InventoryLogAdmin(admin.ModelAdmin):
    list_display = ('inventory', 'action', 'performed_by', 'created_at')
