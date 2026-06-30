from django.db import models
from common.models import BaseModel


class Cart(BaseModel):
    buyer = models.OneToOneField(
        'buyers.BuyerProfile',
        on_delete=models.CASCADE,
        related_name='cart',
    )

    class Meta:
        db_table = 'carts'
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    def __str__(self):
        return f'Cart - {self.buyer.full_name}'

    @property
    def total_items(self):
        return self.items.count()

    @property
    def total_amount(self):
        return sum(item.total_price for item in self.items.all())


class CartItem(BaseModel):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='items',
    )
    seller = models.ForeignKey(
        'sellers.SellerProfile',
        on_delete=models.CASCADE,
    )
    variant = models.ForeignKey(
        'product_variants.ProductVariant',
        on_delete=models.CASCADE,
    )
    quantity = models.IntegerField(default=1)
    unit_price = models.DecimalField(max_digits=12, decimal_places=2)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2, default=18.00)
    shipping_charge = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    notes = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        db_table = 'cart_items'
        verbose_name = 'Cart Item'
        verbose_name_plural = 'Cart Items'
        unique_together = ('cart', 'seller', 'variant')

    def __str__(self):
        return f'{self.variant.name} x{self.quantity}'

    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.unit_price
        super().save(*args, **kwargs)
