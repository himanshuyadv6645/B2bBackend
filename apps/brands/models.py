from django.db import models
from django.utils.text import slugify
from common.models import BaseModel


class Brand(BaseModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True, db_index=True)
    logo = models.URLField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    website = models.URLField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True, db_index=True)
    is_featured = models.BooleanField(default=False)
    sort_order = models.IntegerField(default=0)
    image = models.URLField(max_length=500, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    founded_year = models.IntegerField(null=True, blank=True)
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        db_table = 'brands'
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'
        ordering = ['sort_order', 'name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            original_slug = self.slug
            counter = 1
            while Brand.objects.filter(slug=self.slug).exclude(id=self.id).exists():
                self.slug = f'{original_slug}-{counter}'
                counter += 1
        super().save(*args, **kwargs)

    @property
    def product_count(self):
        from apps.products.models import Product
        return Product.objects.filter(
            brand=self,
            is_active=True,
            deleted_at__isnull=True,
        ).count()
