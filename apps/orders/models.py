import uuid
from django.db import models
from django.utils import timezone
from common.models import SoftDeleteModel, BaseModel


class Order(SoftDeleteModel):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
        ('returned', 'Returned'),
        ('refunded', 'Refunded'),
    )
    PAYMENT_STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('partially_paid', 'Partially Paid'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded'),
        ('partially_refunded', 'Partially Refunded'),
    )

    order_number = models.CharField(max_length=50, unique=True, db_index=True)
    buyer = models.ForeignKey(
        'buyers.BuyerProfile',
        on_delete=models.PROTECT,
        related_name='orders',
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', db_index=True)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending')
    billing_address = models.ForeignKey(
        'buyers.BuyerAddress',
        on_delete=models.PROTECT,
        related_name='billing_orders',
    )
    shipping_address = models.ForeignKey(
        'buyers.BuyerAddress',
        on_delete=models.PROTECT,
        related_name='shipping_orders',
    )
    subtotal = models.DecimalField(max_digits=12, decimal_places=2)
    total_tax = models.DecimalField(max_digits=12, decimal_places=2)
    total_shipping = models.DecimalField(max_digits=12, decimal_places=2)
    total_discount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    notes = models.TextField(blank=True, null=True)
    cancellation_reason = models.TextField(blank=True, null=True)
    cancelled_at = models.DateTimeField(blank=True, null=True)
    delivered_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'orders'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.order_number} - {self.buyer.full_name}'


class OrderItem(BaseModel):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items',
    )
    seller = models.ForeignKey(
        'sellers.SellerProfile',
        on_delete=models.PROTECT,
        related_name='order_items',
    )
    variant = models.ForeignKey(
        'product_variants.ProductVariant',
        on_delete=models.PROTECT,
    )
    product_name = models.CharField(max_length=300)
    variant_name = models.CharField(max_length=300)
    product_image = models.URLField(max_length=500, blank=True, null=True)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=12, decimal_places=2)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=2)
    shipping_charge = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    discount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=Order.STATUS_CHOICES,
        default='pending',
    )

    class Meta:
        db_table = 'order_items'
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'

    def __str__(self):
        return f'{self.product_name} x{self.quantity}'


class SellerOrder(BaseModel):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='seller_orders',
    )
    seller = models.ForeignKey(
        'sellers.SellerProfile',
        on_delete=models.PROTECT,
        related_name='seller_orders',
    )
    status = models.CharField(
        max_length=20,
        choices=Order.STATUS_CHOICES,
        default='pending',
    )
    subtotal = models.DecimalField(max_digits=12, decimal_places=2)
    total_tax = models.DecimalField(max_digits=12, decimal_places=2)
    total_shipping = models.DecimalField(max_digits=12, decimal_places=2)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    shipping_address_snapshot = models.JSONField(blank=True, null=True)
    warehouse = models.ForeignKey(
        'sellers.SellerWarehouse',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    tracking_number = models.CharField(max_length=100, blank=True, null=True)
    tracking_url = models.URLField(max_length=500, blank=True, null=True)
    shipped_at = models.DateTimeField(blank=True, null=True)
    delivered_at = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'seller_orders'
        verbose_name = 'Seller Order'
        verbose_name_plural = 'Seller Orders'

    def __str__(self):
        return f'SellerOrder - {self.seller.company_name} - {self.order.order_number}'


class Invoice(BaseModel):
    invoice_number = models.CharField(max_length=50, unique=True, db_index=True)
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='invoices',
    )
    seller_order = models.ForeignKey(
        SellerOrder,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    seller = models.ForeignKey(
        'sellers.SellerProfile',
        on_delete=models.PROTECT,
        related_name='invoices',
    )
    buyer = models.ForeignKey(
        'buyers.BuyerProfile',
        on_delete=models.PROTECT,
        related_name='invoices',
    )
    subtotal = models.DecimalField(max_digits=12, decimal_places=2)
    cgst = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    sgst = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    igst = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    total_tax = models.DecimalField(max_digits=12, decimal_places=2)
    total_discount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    billing_snapshot = models.JSONField(blank=True, null=True)
    seller_snapshot = models.JSONField(blank=True, null=True)
    pdf_url = models.URLField(max_length=500, blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=(
            ('draft', 'Draft'),
            ('generated', 'Generated'),
            ('sent', 'Sent'),
            ('paid', 'Paid'),
        ),
        default='draft',
    )
    issued_at = models.DateTimeField(blank=True, null=True)
    paid_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'invoices'
        verbose_name = 'Invoice'
        verbose_name_plural = 'Invoices'

    def __str__(self):
        return f'{self.invoice_number}'
