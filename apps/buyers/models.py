import uuid
from django.db import models
from django.conf import settings
from backend.common.models import BaseModel
from backend.common.validators import validate_gstin, validate_pan, validate_phone, validate_pincode


class BuyerProfile(BaseModel):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='buyer_profile',
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True, null=True)
    avatar = models.URLField(max_length=500, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    gstin = models.CharField(max_length=20, unique=True, blank=True, null=True, validators=[validate_gstin])
    pan_number = models.CharField(max_length=10, blank=True, null=True, validators=[validate_pan])
    business_type = models.CharField(max_length=100, blank=True, null=True)
    is_verified = models.BooleanField(default=False)

    class Meta:
        db_table = 'buyer_profiles'
        verbose_name = 'Buyer Profile'
        verbose_name_plural = 'Buyer Profiles'

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.user.email})'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class BuyerAddress(BaseModel):
    ADDRESS_TYPE_CHOICES = (
        ('billing', 'Billing'),
        ('shipping', 'Shipping'),
    )

    buyer = models.ForeignKey(
        BuyerProfile,
        on_delete=models.CASCADE,
        related_name='addresses',
    )
    address_type = models.CharField(max_length=10, choices=ADDRESS_TYPE_CHOICES)
    label = models.CharField(max_length=50, blank=True, null=True)
    contact_name = models.CharField(max_length=200)
    contact_phone = models.CharField(max_length=15, validators=[validate_phone])
    address_line1 = models.CharField(max_length=500)
    address_line2 = models.CharField(max_length=500, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10, validators=[validate_pincode])
    country = models.CharField(max_length=50, default='India')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    is_default = models.BooleanField(default=False)

    class Meta:
        db_table = 'buyer_addresses'
        verbose_name = 'Buyer Address'
        verbose_name_plural = 'Buyer Addresses'
        ordering = ['-is_default', '-created_at']

    def __str__(self):
        return f'{self.label or self.address_type}: {self.address_line1}, {self.city}'

    def save(self, *args, **kwargs):
        if self.is_default:
            BuyerAddress.objects.filter(
                buyer=self.buyer,
                address_type=self.address_type,
                is_default=True,
            ).exclude(id=self.id).update(is_default=False)
        super().save(*args, **kwargs)
