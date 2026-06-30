import random
import uuid
from decimal import Decimal, ROUND_HALF_UP
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.utils.text import slugify

from apps.sellers.models import SellerProfile, SellerWarehouse
from apps.categories.models import Category
from apps.brands.models import Brand
from apps.products.models import Product, ProductAttribute, ProductImage
from apps.product_variants.models import ProductVariant, VariantAttribute, VariantImage
from apps.pricing.models import SellerPricing, WholesaleTier
from apps.inventory.models import Inventory
from apps.products.management.commands.catalog_data import (
    BRANDS, PRODUCTS, IMAGES,
)


def get_images(img_key, count=3):
    urls = IMAGES.get(img_key, IMAGES['default'])
    return [urls[i % len(urls)] for i in range(count)]


class Command(BaseCommand):
    help = 'Seed 500+ products with brands, variants, pricing, inventory'

    def add_arguments(self, parser):
        parser.add_argument('--clear', action='store_true', help='Clear product data first')

    def handle(self, *args, **options):
        if options['clear']:
            self.stdout.write('Clearing product data...')
            from django.db import connection
            with connection.cursor() as cursor:
                for table in [
                    'product_reviews', 'seller_reviews', 'order_items', 'seller_orders',
                    'invoices', 'orders', 'cart_items', 'carts', 'stock_history',
                    'inventory_logs', 'inventory', 'wholesale_tiers', 'seller_pricing',
                    'variant_images', 'variant_attributes', 'product_variants',
                    'product_images', 'product_attributes', 'products',
                ]:
                    try:
                        cursor.execute(f'TRUNCATE TABLE {table} CASCADE')
                    except Exception:
                        pass
            self.stdout.write(self.style.SUCCESS('Cleared.'))

        self.stdout.write(self.style.WARNING('\nSeeding Product Catalog...\n'))

        self.brand_map = {}
        self._create_brands()
        self._create_products()

        self.stdout.write(self.style.SUCCESS(
            f'\nDone! Brands: {Brand.objects.count()}, '
            f'Products: {Product.objects.count()}, '
            f'Variants: {ProductVariant.objects.count()}, '
            f'Images: {ProductImage.objects.count()}, '
            f'Attributes: {ProductAttribute.objects.count()}\n'
        ))

    def _create_brands(self):
        self.stdout.write('Creating brands...')
        for name, country, founded, featured, desc in BRANDS:
            brand, _ = Brand.objects.update_or_create(
                name=name,
                defaults={
                    'country': country,
                    'founded_year': founded,
                    'is_featured': featured,
                    'description': desc,
                    'is_active': True,
                    'meta_title': f'{name} - B2B Wholesale',
                    'meta_description': f'Buy {name} products at best wholesale prices.',
                },
            )
            self.brand_map[name] = brand
        self.stdout.write(f'  {len(self.brand_map)} brands')

    def _find_category(self, name):
        cat = Category.objects.filter(name__iexact=name, deleted_at__isnull=True).first()
        if not cat:
            cat = Category.objects.filter(name__icontains=name.split()[0], deleted_at__isnull=True).first()
        return cat

    def _create_products(self):
        self.stdout.write('Creating products (bulk)...')
        sellers = list(SellerProfile.objects.filter(status='approved'))
        now = timezone.now()

        # Build all product objects
        products_to_create = []
        attributes_to_create = []
        images_to_create = []
        variants_to_create = []
        variant_attrs_to_create = []
        variant_images_to_create = []
        pricing_to_create = []
        tiers_to_create = []
        inventory_to_create = []

        # Get existing slugs
        existing_slugs = set(Product.all_objects.values_list('slug', flat=True))

        product_count = 0

        for cat_name, products_list in PRODUCTS.items():
            cat = self._find_category(cat_name)
            if not cat:
                continue

            for prod_data in products_list:
                (name, brand_name, sku_suffix, short_desc,
                 retail_price, moq, gst, warranty, country,
                 img_key, specs) = prod_data

                slug = slugify(name)
                if slug in existing_slugs:
                    continue
                existing_slugs.add(slug)

                brand = self.brand_map.get(brand_name)
                wholesale_price = (Decimal(str(retail_price)) * Decimal('0.75')).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
                selling_price = (wholesale_price * Decimal('1.10')).quantize(Decimal('1'), rounding=ROUND_HALF_UP)

                pid = uuid.uuid4()
                is_feat = random.random() < 0.15
                is_trend = random.random() < 0.10
                is_top = random.random() < 0.10
                stock = random.randint(20, 500)
                rating = round(random.uniform(3.5, 4.9), 2)
                reviews = random.randint(5, 200)

                products_to_create.append(Product(
                    id=pid,
                    name=name,
                    slug=slug,
                    sku=f'B2B-{sku_suffix}',
                    category=cat,
                    brand=brand,
                    description=f'{name} - {short_desc}. Best wholesale price for B2B buyers.',
                    short_description=short_desc,
                    hsn_code='8471',
                    retail_price=Decimal(str(retail_price)),
                    wholesale_price=wholesale_price,
                    min_selling_price=selling_price,
                    max_selling_price=Decimal(str(retail_price)),
                    gst=Decimal(str(gst)),
                    moq=moq,
                    warranty=warranty,
                    country_of_origin=country,
                    specifications=specs,
                    is_active=True,
                    is_featured=is_feat,
                    is_trending=is_trend,
                    is_top_seller=is_top,
                    total_stock=stock,
                    average_rating=Decimal(str(rating)),
                    total_reviews=reviews,
                    created_at=now,
                    updated_at=now,
                ))
                product_count += 1

                # Attributes
                for i, (k, v) in enumerate(specs.items()):
                    attributes_to_create.append(ProductAttribute(
                        id=uuid.uuid4(),
                        product_id=pid,
                        key=k,
                        value=v,
                        sort_order=i,
                    ))

                # Images
                img_urls = get_images(img_key, 3)
                for i, url in enumerate(img_urls):
                    images_to_create.append(ProductImage(
                        id=uuid.uuid4(),
                        product_id=pid,
                        image_url=url,
                        alt_text=f'{name} image {i+1}',
                        sort_order=i,
                        is_primary=(i == 0),
                    ))

                # Variant
                vid = uuid.uuid4()
                variants_to_create.append(ProductVariant(
                    id=vid,
                    product_id=pid,
                    name=f'{name} - Standard',
                    sku=f'B2B-{sku_suffix}-STD',
                    description=f'Standard variant of {name}',
                    slug=slugify(f'{name}-standard'),
                    is_active=True,
                    min_selling_price=selling_price,
                    max_selling_price=Decimal(str(retail_price)),
                    total_stock=stock,
                    average_rating=Decimal(str(rating)),
                    created_at=now,
                    updated_at=now,
                ))

                variant_attrs_to_create.append(VariantAttribute(
                    id=uuid.uuid4(),
                    variant_id=vid,
                    attribute_name='SKU',
                    attribute_value=f'B2B-{sku_suffix}-STD',
                ))

                variant_images_to_create.append(VariantImage(
                    id=uuid.uuid4(),
                    variant_id=vid,
                    image_url=img_urls[0],
                    alt_text=name,
                    is_primary=True,
                ))

                # Pricing + Wholesale Tiers (assign to 1-2 sellers)
                for seller in sellers[:random.randint(1, min(2, len(sellers)))]:
                    spid = uuid.uuid4()
                    pricing_to_create.append(SellerPricing(
                        id=spid,
                        seller=seller,
                        variant_id=vid,
                        selling_price=selling_price,
                        tax_rate=Decimal(str(gst)),
                        tax_inclusive=False,
                        minimum_order_quantity=moq,
                        is_active=True,
                        delivery_time_days=random.randint(1, 5),
                        estimated_delivery=f'{random.randint(2, 7)} business days',
                        created_at=now,
                        updated_at=now,
                    ))

                    tiers = [
                        (1, 4, selling_price),
                        (5, 9, (selling_price * Decimal('0.96')).quantize(Decimal('1'))),
                        (10, 24, (selling_price * Decimal('0.92')).quantize(Decimal('1'))),
                        (25, 49, (selling_price * Decimal('0.88')).quantize(Decimal('1'))),
                        (50, None, (selling_price * Decimal('0.84')).quantize(Decimal('1'))),
                    ]
                    for min_q, max_q, price in tiers:
                        tiers_to_create.append(WholesaleTier(
                            id=uuid.uuid4(),
                            pricing_id=spid,
                            min_quantity=min_q,
                            max_quantity=max_q,
                            price_per_unit=price,
                            discount_percent=Decimal(str(round((1 - price / selling_price) * 100, 1))),
                            created_at=now,
                            updated_at=now,
                        ))

                    # Inventory
                    wh = SellerWarehouse.objects.filter(seller=seller, is_active=True).first()
                    if wh:
                        inventory_to_create.append(Inventory(
                            id=uuid.uuid4(),
                            seller=seller,
                            variant_id=vid,
                            warehouse=wh,
                            total_stock=stock,
                            available_stock=stock,
                            created_at=now,
                            updated_at=now,
                        ))

        self.stdout.write(f'  Built {product_count} products in memory. Bulk inserting...')

        # Bulk create in batches
        BATCH = 500

        for i in range(0, len(products_to_create), BATCH):
            Product.all_objects.bulk_create(products_to_create[i:i+BATCH], batch_size=BATCH)
        self.stdout.write(f'  Products: {len(products_to_create)}')

        for i in range(0, len(attributes_to_create), BATCH):
            ProductAttribute.objects.bulk_create(attributes_to_create[i:i+BATCH], batch_size=BATCH)
        self.stdout.write(f'  Attributes: {len(attributes_to_create)}')

        for i in range(0, len(images_to_create), BATCH):
            ProductImage.objects.bulk_create(images_to_create[i:i+BATCH], batch_size=BATCH)
        self.stdout.write(f'  Images: {len(images_to_create)}')

        for i in range(0, len(variants_to_create), BATCH):
            ProductVariant.all_objects.bulk_create(variants_to_create[i:i+BATCH], batch_size=BATCH)
        self.stdout.write(f'  Variants: {len(variants_to_create)}')

        for i in range(0, len(variant_attrs_to_create), BATCH):
            VariantAttribute.objects.bulk_create(variant_attrs_to_create[i:i+BATCH], batch_size=BATCH)

        for i in range(0, len(variant_images_to_create), BATCH):
            VariantImage.objects.bulk_create(variant_images_to_create[i:i+BATCH], batch_size=BATCH)

        for i in range(0, len(pricing_to_create), BATCH):
            SellerPricing.objects.bulk_create(pricing_to_create[i:i+BATCH], batch_size=BATCH)
        self.stdout.write(f'  Pricing: {len(pricing_to_create)}')

        for i in range(0, len(tiers_to_create), BATCH):
            WholesaleTier.objects.bulk_create(tiers_to_create[i:i+BATCH], batch_size=BATCH)
        self.stdout.write(f'  Wholesale Tiers: {len(tiers_to_create)}')

        for i in range(0, len(inventory_to_create), BATCH):
            Inventory.objects.bulk_create(inventory_to_create[i:i+BATCH], batch_size=BATCH)
        self.stdout.write(f'  Inventory: {len(inventory_to_create)}')

        # Update seller counts
        self.stdout.write('  Updating seller counts...')
        from django.db.models import Count, Q
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute('''
                UPDATE products SET total_sellers = (
                    SELECT COUNT(DISTINCT sp.seller_id)
                    FROM seller_pricing sp
                    WHERE sp.variant_id IN (
                        SELECT pv.id FROM product_variants pv WHERE pv.product_id = products.id
                    ) AND sp.is_active = true
                )
            ''')
        self.stdout.write('  Done!')
