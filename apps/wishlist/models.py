from django.db import models
from common.models import BaseModel


class Wishlist(BaseModel):
    buyer = models.ForeignKey(
        'buyers.BuyerProfile',
        on_delete=models.CASCADE,
        related_name='wishlist',
    )
    variant = models.ForeignKey(
        'product_variants.ProductVariant',
        on_delete=models.CASCADE,
        related_name='wishlisted_by',
    )

    class Meta:
        db_table = 'wishlists'
        verbose_name = 'Wishlist'
        verbose_name_plural = 'Wishlists'
        unique_together = ('buyer', 'variant')

    def __str__(self):
        return f'{self.buyer.full_name} - {self.variant.name}'
