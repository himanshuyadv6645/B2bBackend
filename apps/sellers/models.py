import uuid
from django.db import models
from django.conf import settings
from common.models import BaseModel
from common.validators import validate_gstin, validate_pan, validate_phone, validate_pincode


class SellerProfile(BaseModel):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('suspended', 'Suspended'),
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='seller_profile',
    )
    company_name = models.CharField(max_length=255)
    gstin = models.CharField(max_length=20, unique=True, blank=True, null=True, validators=[validate_gstin])
    pan_number = models.CharField(max_length=10, blank=True, null=True, validators=[validate_pan])
    contact_name = models.CharField(max_length=200)
    contact_phone = models.CharField(max_length=15, validators=[validate_phone])
    logo = models.URLField(max_length=500, blank=True, null=True)
    banner = models.URLField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    business_type = models.CharField(max_length=100, blank=True, null=True)
    website = models.URLField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending', db_index=True)
    approval_date = models.DateTimeField(blank=True, null=True)
    rejection_reason = models.TextField(blank=True, null=True)
    commission_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    total_ratings = models.IntegerField(default=0)
    is_verified = models.BooleanField(default=False)

    class Meta:
        db_table = 'seller_profiles'
        verbose_name = 'Seller Profile'
        verbose_name_plural = 'Seller Profiles'

    def __str__(self):
        return f'{self.company_name} ({self.status})'


class SellerWarehouse(BaseModel):
    seller = models.ForeignKey(
        SellerProfile,
        on_delete=models.CASCADE,
        related_name='warehouses',
    )
    name = models.CharField(max_length=200)
    contact_phone = models.CharField(max_length=15, validators=[validate_phone])
    address_line1 = models.CharField(max_length=500)
    address_line2 = models.CharField(max_length=500, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10, validators=[validate_pincode])
    country = models.CharField(max_length=50, default='India')
    latitude = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    longitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_primary = models.BooleanField(default=False)

    class Meta:
        db_table = 'seller_warehouses'
        verbose_name = 'Seller Warehouse'
        verbose_name_plural = 'Seller Warehouses'

    def __str__(self):
        return f'{self.name} - {self.seller.company_name}'

    def save(self, *args, **kwargs):
        if self.is_primary:
            SellerWarehouse.objects.filter(
                seller=self.seller,
                is_primary=True,
            ).exclude(id=self.id).update(is_primary=False)
        super().save(*args, **kwargs)
