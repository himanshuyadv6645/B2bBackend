from django.contrib import admin
from .models import Order, OrderItem, SellerOrder, Invoice


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['product_name', 'variant_name', 'quantity', 'unit_price', 'tax_amount', 'total_price']


class SellerOrderInline(admin.TabularInline):
    model = SellerOrder
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'buyer', 'status', 'payment_status', 'total_amount', 'created_at')
    list_filter = ('status', 'payment_status')
    search_fields = ('order_number', 'buyer__first_name', 'buyer__last_name')
    inlines = [OrderItemInline, SellerOrderInline]


@admin.register(SellerOrder)
class SellerOrderAdmin(admin.ModelAdmin):
    list_display = ('order', 'seller', 'status', 'total_amount', 'tracking_number')
    list_filter = ('status',)


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_number', 'order', 'seller', 'buyer', 'total_amount', 'status')
    list_filter = ('status',)
