import uuid
from django.db import models
from django.utils.text import slugify
from common.models import SoftDeleteModel


class Product(SoftDeleteModel):
    seller = models.ForeignKey(
        'sellers.SellerProfile',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='listed_products',
    )
    category = models.ForeignKey(
        'categories.Category',
        on_delete=models.PROTECT,
        related_name='products',
    )
    brand = models.ForeignKey(
        'brands.Brand',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='products',
    )
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=350, unique=True, db_index=True)
    description = models.TextField(blank=True, null=True)
    short_description = models.CharField(max_length=500, blank=True, null=True)
    sku = models.CharField(max_length=100, unique=True, db_index=True)
    hsn_code = models.CharField(max_length=20, blank=True, null=True)
    taxable = models.BooleanField(default=True)

    # Pricing
    retail_price = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True,
        help_text='MRP / Retail Price',
    )
    wholesale_price = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True,
        help_text='Base wholesale price',
    )
    min_selling_price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    max_selling_price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    gst = models.DecimalField(
        max_digits=5, decimal_places=2, default=18.00,
        help_text='GST percentage',
    )
    moq = models.IntegerField(
        default=1, help_text='Minimum Order Quantity',
    )

    # Physical attributes
    weight = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True,
        help_text='Weight in kg',
    )
    length = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    width = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    height = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    # Product info
    warranty = models.CharField(max_length=200, blank=True, null=True)
    country_of_origin = models.CharField(max_length=100, default='India')

    # Status flags
    is_active = models.BooleanField(default=True, db_index=True)
    is_featured = models.BooleanField(default=False)
    is_trending = models.BooleanField(default=False, db_index=True)
    is_top_seller = models.BooleanField(default=False, db_index=True)
    is_digital = models.BooleanField(default=False)

    # Specs
    specifications = models.JSONField(
        default=dict, blank=True,
        help_text='Product specifications as JSON',
    )

    # Meta
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.CharField(max_length=500, blank=True, null=True)

    # Aggregates
    total_sellers = models.IntegerField(default=0)
    total_stock = models.IntegerField(default=0)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    total_reviews = models.IntegerField(default=0)
    views_count = models.IntegerField(default=0)

    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['is_featured', 'is_active']),
            models.Index(fields=['is_trending', 'is_active']),
            models.Index(fields=['is_top_seller', 'is_active']),
            models.Index(fields=['category', 'is_active']),
            models.Index(fields=['brand', 'is_active']),
            models.Index(fields=['seller', 'is_active']),
        ]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            original_slug = self.slug
            counter = 1
            while Product.all_objects.filter(slug=self.slug).exclude(id=self.id).exists():
                self.slug = f'{original_slug}-{counter}'
                counter += 1
        super().save(*args, **kwargs)

    @property
    def discount_percent(self):
        if self.retail_price and self.min_selling_price and self.retail_price > 0:
            return round((1 - float(self.min_selling_price) / float(self.retail_price)) * 100)
        return 0


class ProductAttribute(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='attributes',
    )
    key = models.CharField(max_length=200)
    value = models.CharField(max_length=500)
    sort_order = models.IntegerField(default=0)

    class Meta:
        db_table = 'product_attributes'
        ordering = ['sort_order']

    def __str__(self):
        return f'{self.key}: {self.value}'


class ProductImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images',
    )
    image_url = models.URLField(max_length=500)
    alt_text = models.CharField(max_length=255, blank=True, null=True)
    sort_order = models.IntegerField(default=0)
    is_primary = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'product_images'
        ordering = ['sort_order']

    def __str__(self):
        return f'Image for {self.product.name}'


class ProductDocument(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='documents',
    )
    title = models.CharField(max_length=200)
    file_url = models.URLField(max_length=500)
    file_type = models.CharField(max_length=50)
    file_size = models.IntegerField(blank=True, null=True)
    sort_order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'product_documents'
        ordering = ['sort_order']

    def __str__(self):
        return f'{self.title} ({self.file_type})'
