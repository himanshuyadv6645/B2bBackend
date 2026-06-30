from django.contrib import admin
from .models import Payment, Refund


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('order', 'gateway', 'amount', 'status', 'created_at')
    list_filter = ('gateway', 'status')


@admin.register(Refund)
class RefundAdmin(admin.ModelAdmin):
    list_display = ('order', 'payment', 'amount', 'status', 'created_at')
    list_filter = ('status',)
