from django.db import models
from django.utils.text import slugify
from common.models import BaseModel


class SEOPage(BaseModel):
    PAGE_TYPES = [
        ('category', 'Category'),
        ('category_city', 'Category + City'),
        ('category_brand', 'Category + Brand'),
        ('category_brand_city', 'Category + Brand + City'),
        ('brand', 'Brand'),
        ('brand_city', 'Brand + City'),
        ('city', 'City'),
        ('seller', 'Seller'),
        ('search', 'Search'),
    ]

    page_type = models.CharField(max_length=30, choices=PAGE_TYPES, db_index=True)
    slug = models.SlugField(max_length=500, unique=True, db_index=True)

    category = models.ForeignKey(
        'categories.Category',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='seo_pages',
    )
    brand = models.ForeignKey(
        'brands.Brand',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='seo_pages',
    )
    seller = models.ForeignKey(
        'sellers.SellerProfile',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='seo_pages',
    )

    city = models.CharField(max_length=100, blank=True, default='')
    state = models.CharField(max_length=100, blank=True, default='')
    country = models.CharField(max_length=100, blank=True, default='India')

    title = models.CharField(max_length=70)
    meta_description = models.CharField(max_length=160)
    meta_keywords = models.TextField(blank=True, default='')

    h1_heading = models.CharField(max_length=200)
    intro_text = models.TextField(blank=True, default='')
    buying_guide = models.TextField(blank=True, default='')
    why_choose_us = models.TextField(blank=True, default='')
    faq_json = models.JSONField(default=list, blank=True)
    related_searches = models.JSONField(default=list, blank=True)

    canonical_url = models.CharField(max_length=500, blank=True, default='')
    og_title = models.CharField(max_length=200, blank=True, default='')
    og_description = models.CharField(max_length=300, blank=True, default='')
    og_image = models.URLField(max_length=500, blank=True, default='')

    schema_json = models.JSONField(default=dict, blank=True)

    is_active = models.BooleanField(default=True, db_index=True)
    views_count = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['page_type', 'is_active']),
            models.Index(fields=['category', 'city']),
            models.Index(fields=['brand', 'city']),
        ]

    def __str__(self):
        return f"{self.page_type}: {self.slug}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._generate_slug()
        if not self.og_title:
            self.og_title = self.title
        if not self.og_description:
            self.og_description = self.meta_description
        super().save(*args, **kwargs)

    def _generate_slug(self):
        parts = []
        if self.category:
            parts.append(self.category.slug)
        if self.brand:
            parts.append(self.brand.slug)
        if self.city:
            parts.append(slugify(self.city))
        slug = '/'.join(parts) if parts else slugify(self.title)
        return slug


class SEOFAQ(BaseModel):
    page = models.ForeignKey(SEOPage, on_delete=models.CASCADE, related_name='faqs')
    question = models.CharField(max_length=300)
    answer = models.TextField()
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['sort_order']

    def __str__(self):
        return self.question[:60]
