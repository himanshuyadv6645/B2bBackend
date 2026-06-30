from django.db import models
from django.utils.text import slugify
from common.models import BaseModel


class Category(BaseModel):
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children',
    )
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True, db_index=True)
    description = models.TextField(blank=True, null=True)
    image = models.URLField(max_length=500, blank=True, null=True)
    thumbnail = models.URLField(max_length=500, blank=True, null=True)
    icon = models.CharField(max_length=200, blank=True, null=True)
    sort_order = models.IntegerField(default=0, db_index=True)
    is_active = models.BooleanField(default=True, db_index=True)
    is_featured = models.BooleanField(default=False, db_index=True)
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    keywords = models.TextField(
        blank=True, null=True,
        help_text='Comma-separated aliases, misspellings, and related terms for search matching',
    )
    level = models.IntegerField(default=0, db_index=True)
    path = models.CharField(max_length=500, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True, db_index=True)

    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['sort_order', 'name']
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'parent'],
                name='unique_category_name_per_parent',
            ),
        ]
        indexes = [
            models.Index(fields=['parent', 'is_active']),
            models.Index(fields=['level', 'is_active']),
            models.Index(fields=['is_featured', 'is_active']),
        ]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            original_slug = self.slug
            counter = 1
            while Category.objects.filter(slug=self.slug).exclude(id=self.id).exists():
                self.slug = f'{original_slug}-{counter}'
                counter += 1

        if self.parent:
            self.level = self.parent.level + 1
            self.path = f'{self.parent.path}/{self.slug}' if self.parent.path else f'/{self.parent.slug}/{self.slug}'
        else:
            self.level = 0
            self.path = f'/{self.slug}'

        super().save(*args, **kwargs)

    @property
    def is_root(self):
        return self.parent is None

    @property
    def get_ancestors(self):
        ancestors = []
        current = self.parent
        while current:
            ancestors.insert(0, current)
            current = current.parent
        return ancestors

    @property
    def get_descendants(self):
        descendants = list(self.children.filter(is_active=True, deleted_at__isnull=True))
        for child in list(descendants):
            descendants.extend(child.get_descendants)
        return descendants

    @property
    def product_count(self):
        from apps.products.models import Product
        return Product.objects.filter(
            category=self,
            is_active=True,
            deleted_at__isnull=True,
        ).count()

    def soft_delete(self):
        from django.utils import timezone
        self.deleted_at = timezone.now()
        self.save(update_fields=['deleted_at'])
