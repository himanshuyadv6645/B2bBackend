import uuid
from django.db import models
from common.models import BaseModel


class Inventory(BaseModel):
    seller = models.ForeignKey(
        'sellers.SellerProfile',
        on_delete=models.CASCADE,
        related_name='inventory',
    )
    variant = models.ForeignKey(
        'product_variants.ProductVariant',
        on_delete=models.CASCADE,
        related_name='inventory',
    )
    warehouse = models.ForeignKey(
        'sellers.SellerWarehouse',
        on_delete=models.CASCADE,
        related_name='inventory',
    )
    total_stock = models.IntegerField(default=0)
    reserved_stock = models.IntegerField(default=0)
    available_stock = models.IntegerField(default=0)
    low_stock_threshold = models.IntegerField(default=10)

    class Meta:
        db_table = 'inventory'
        verbose_name = 'Inventory'
        verbose_name_plural = 'Inventory'
        unique_together = ('seller', 'variant', 'warehouse')

    def __str__(self):
        return f'{self.seller.company_name} - {self.variant.name}: {self.available_stock}'

    def save(self, *args, **kwargs):
        self.available_stock = self.total_stock - self.reserved_stock
        super().save(*args, **kwargs)

    @property
    def is_in_stock(self):
        return self.available_stock > 0

    @property
    def is_low_stock(self):
        return self.available_stock <= self.low_stock_threshold


class StockHistory(BaseModel):
    CHANGE_TYPE_CHOICES = (
        ('add', 'Add'),
        ('remove', 'Remove'),
        ('reserved', 'Reserved'),
        ('unreserved', 'Unreserved'),
        ('adjustment', 'Adjustment'),
    )

    inventory = models.ForeignKey(
        Inventory,
        on_delete=models.CASCADE,
        related_name='stock_history',
    )
    change_type = models.CharField(max_length=20, choices=CHANGE_TYPE_CHOICES)
    quantity_change = models.IntegerField()
    previous_stock = models.IntegerField()
    new_stock = models.IntegerField()
    reference_type = models.CharField(max_length=50, blank=True, null=True)
    reference_id = models.UUIDField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'stock_history'
        verbose_name = 'Stock History'
        verbose_name_plural = 'Stock History'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.change_type}: {self.quantity_change} for {self.inventory}'


class InventoryLog(BaseModel):
    inventory = models.ForeignKey(
        Inventory,
        on_delete=models.CASCADE,
        related_name='logs',
    )
    action = models.CharField(max_length=100)
    old_values = models.JSONField(blank=True, null=True)
    new_values = models.JSONField(blank=True, null=True)
    performed_by = models.ForeignKey(
        'authentication.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    ip_address = models.GenericIPAddressField(blank=True, null=True)

    class Meta:
        db_table = 'inventory_logs'
        verbose_name = 'Inventory Log'
        verbose_name_plural = 'Inventory Logs'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.action} on {self.inventory}'
