from django.db import models
from common.models import BaseModel


class Banner(BaseModel):
    PLACEMENT_CHOICES = (
        ('homepage', 'Homepage'),
        ('category', 'Category Page'),
        ('subcategory', 'Subcategory Page'),
        ('product', 'Product Page'),
        ('seller', 'Seller Page'),
        ('checkout', 'Checkout Page'),
        ('popup', 'Popup'),
        ('sidebar', 'Sidebar'),
    )

    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=500, blank=True, null=True)
    image = models.URLField(max_length=500)
    mobile_image = models.URLField(max_length=500, blank=True, null=True)

    link_url = models.URLField(max_length=500, blank=True, null=True)
    link_text = models.CharField(max_length=100, blank=True, null=True)

    placement = models.CharField(max_length=20, choices=PLACEMENT_CHOICES, db_index=True)
    sort_order = models.IntegerField(default=0, db_index=True)

    category = models.ForeignKey(
        'categories.Category',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='banners',
    )
    brand = models.ForeignKey(
        'brands.Brand',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='banners',
    )
    seller = models.ForeignKey(
        'sellers.SellerProfile',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='banners',
    )

    is_active = models.BooleanField(default=True, db_index=True)
    start_date = models.DateTimeField(null=True, blank=True, db_index=True)
    end_date = models.DateTimeField(null=True, blank=True, db_index=True)

    meta = models.JSONField(blank=True, null=True)

    class Meta:
        db_table = 'banners'
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'
        ordering = ['sort_order', '-created_at']
        indexes = [
            models.Index(fields=['placement', 'is_active']),
            models.Index(fields=['is_active', 'start_date', 'end_date']),
        ]

    def __str__(self):
        return f'{self.title} ({self.get_placement_display()})'

    @property
    def is_currently_active(self):
        from django.utils import timezone
        now = timezone.now()
        if not self.is_active:
            return False
        if self.start_date and now < self.start_date:
            return False
        if self.end_date and now > self.end_date:
            return False
        return True
