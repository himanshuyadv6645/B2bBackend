import uuid
from django.db import models
from django.utils.text import slugify
from common.models import SoftDeleteModel


class ProductVariant(SoftDeleteModel):
    product = models.ForeignKey(
        'products.Product',
        on_delete=models.CASCADE,
        related_name='variants',
    )
    sku = models.CharField(max_length=150, unique=True, db_index=True)
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=350, unique=True, db_index=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    sort_order = models.IntegerField(default=0)
    min_selling_price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    max_selling_price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    total_sellers = models.IntegerField(default=0)
    total_stock = models.IntegerField(default=0)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)

    class Meta:
        db_table = 'product_variants'
        verbose_name = 'Product Variant'
        verbose_name_plural = 'Product Variants'
        ordering = ['sort_order', 'name']

    def __str__(self):
        return f'{self.product.name} - {self.name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            original_slug = self.slug
            counter = 1
            while ProductVariant.all_objects.filter(slug=self.slug).exclude(id=self.id).exists():
                self.slug = f'{original_slug}-{counter}'
                counter += 1
        super().save(*args, **kwargs)


class VariantAttribute(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    variant = models.ForeignKey(
        ProductVariant,
        on_delete=models.CASCADE,
        related_name='attributes',
    )
    attribute_name = models.CharField(max_length=200)
    attribute_value = models.CharField(max_length=200)

    class Meta:
        db_table = 'variant_attributes'
        verbose_name = 'Variant Attribute'
        verbose_name_plural = 'Variant Attributes'

    def __str__(self):
        return f'{self.attribute_name}: {self.attribute_value}'


class VariantImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    variant = models.ForeignKey(
        ProductVariant,
        on_delete=models.CASCADE,
        related_name='images',
    )
    image_url = models.URLField(max_length=500)
    alt_text = models.CharField(max_length=255, blank=True, null=True)
    sort_order = models.IntegerField(default=0)
    is_primary = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'variant_images'
        ordering = ['sort_order']

    def __str__(self):
        return f'Image for {self.variant.name}'
