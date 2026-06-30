from django.db import models
from common.models import BaseModel


class SellerPricing(BaseModel):
    seller = models.ForeignKey(
        'sellers.SellerProfile',
        on_delete=models.CASCADE,
        related_name='pricing',
    )
    variant = models.ForeignKey(
        'product_variants.ProductVariant',
        on_delete=models.CASCADE,
        related_name='seller_pricing',
    )
    warehouse = models.ForeignKey(
        'sellers.SellerWarehouse',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    selling_price = models.DecimalField(max_digits=12, decimal_places=2)
    offer_price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2, default=18.00)
    tax_inclusive = models.BooleanField(default=False)
    shipping_charge = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    free_shipping = models.BooleanField(default=False)
    minimum_order_quantity = models.IntegerField(default=1)
    max_order_quantity = models.IntegerField(null=True, blank=True)
    warranty_type = models.CharField(max_length=50, blank=True, null=True)
    warranty_period = models.CharField(max_length=50, blank=True, null=True)
    delivery_time_days = models.IntegerField(null=True, blank=True)
    estimated_delivery = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    valid_from = models.DateTimeField(null=True, blank=True)
    valid_till = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'seller_pricing'
        verbose_name = 'Seller Pricing'
        verbose_name_plural = 'Seller Pricing'
        unique_together = ('seller', 'variant')
        ordering = ['selling_price']

    def __str__(self):
        return f'{self.seller.company_name} - {self.variant.name} @ {self.selling_price}'

    def get_wholesale_price(self, quantity):
        from django.db.models import Q
        tier = self.wholesale_tiers.filter(
            min_quantity__lte=quantity,
        ).filter(
            Q(max_quantity__gte=quantity) | Q(max_quantity__isnull=True)
        ).order_by('-min_quantity').first()
        if tier:
            return tier.price_per_unit
        return None


class WholesaleTier(BaseModel):
    pricing = models.ForeignKey(
        SellerPricing,
        on_delete=models.CASCADE,
        related_name='wholesale_tiers',
    )
    min_quantity = models.IntegerField(help_text='Minimum quantity for this tier (inclusive)')
    max_quantity = models.IntegerField(null=True, blank=True, help_text='Maximum quantity (inclusive). NULL = unlimited')
    price_per_unit = models.DecimalField(max_digits=12, decimal_places=2, help_text='Price per unit at this tier')
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, help_text='Discount % off MRP')
    notes = models.CharField(max_length=200, blank=True, null=True, help_text='Internal notes for this tier')

    class Meta:
        db_table = 'wholesale_tiers'
        verbose_name = 'Wholesale Tier'
        verbose_name_plural = 'Wholesale Tiers'
        ordering = ['min_quantity']
        constraints = [
            models.UniqueConstraint(
                fields=['pricing', 'min_quantity'],
                name='unique_tier_per_pricing',
            ),
        ]

    def __str__(self):
        max_qty = self.max_quantity or '∞'
        return f'{self.min_quantity}-{max_qty} units @ ₹{self.price_per_unit}/unit'

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.max_quantity and self.min_quantity > self.max_quantity:
            raise ValidationError('min_quantity cannot be greater than max_quantity')

    @property
    def range_display(self):
        if self.max_quantity:
            return f'{self.min_quantity} - {self.max_quantity} units'
        return f'{self.min_quantity}+ units'
