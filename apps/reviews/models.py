from django.db import models
from common.models import BaseModel
from common.validators import validate_rating


class ProductReview(BaseModel):
    product = models.ForeignKey(
        'products.Product',
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    variant = models.ForeignKey(
        'product_variants.ProductVariant',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    buyer = models.ForeignKey(
        'buyers.BuyerProfile',
        on_delete=models.CASCADE,
    )
    order_item = models.ForeignKey(
        'orders.OrderItem',
        on_delete=models.CASCADE,
    )
    seller = models.ForeignKey(
        'sellers.SellerProfile',
        on_delete=models.CASCADE,
        related_name='product_reviews',
    )
    rating = models.SmallIntegerField(validators=[validate_rating])
    title = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    images = models.JSONField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')],
        default='pending',
        db_index=True
    )

    class Meta:
        db_table = 'product_reviews'
        verbose_name = 'Product Review'
        verbose_name_plural = 'Product Reviews'
        unique_together = ('buyer', 'order_item')
        ordering = ['-created_at']

    def __str__(self):
        return f'Review by {self.buyer.full_name} for {self.product.name}'


class SellerReview(BaseModel):
    seller = models.ForeignKey(
        'sellers.SellerProfile',
        on_delete=models.CASCADE,
        related_name='seller_reviews',
    )
    buyer = models.ForeignKey(
        'buyers.BuyerProfile',
        on_delete=models.CASCADE,
    )
    order = models.ForeignKey(
        'orders.Order',
        on_delete=models.CASCADE,
    )
    rating = models.SmallIntegerField(validators=[validate_rating])
    title = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')],
        default='pending',
        db_index=True
    )

    class Meta:
        db_table = 'seller_reviews'
        verbose_name = 'Seller Review'
        verbose_name_plural = 'Seller Reviews'
        unique_together = ('buyer', 'order', 'seller')
        ordering = ['-created_at']

    def __str__(self):
        return f'Review by {self.buyer.full_name} for {self.seller.company_name}'
