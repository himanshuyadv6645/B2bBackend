from apps.products.models import Product, ProductAttribute, ProductImage, ProductDocument


class ProductService:
    @staticmethod
    def get_product_by_slug(slug):
        try:
            return Product.objects.get(slug=slug, is_active=True, deleted_at__isnull=True)
        except Product.DoesNotExist:
            return None

    @staticmethod
    def update_product_stats(product_id):
        product = Product.objects.get(id=product_id)
        from apps.pricing.models import SellerPricing
        from apps.inventory.models import Inventory

        pricing = SellerPricing.objects.filter(variant__product=product, is_active=True)
        if pricing.exists():
            prices = pricing.values_list('selling_price', flat=True)
            product.min_selling_price = min(prices)
            product.max_selling_price = max(prices)
            product.total_sellers = pricing.values('seller').distinct().count()
        
        inventory = Inventory.objects.filter(variant__product=product)
        product.total_stock = sum(inv.available_stock for inv in inventory)
        product.save(update_fields=[
            'min_selling_price', 'max_selling_price',
            'total_sellers', 'total_stock', 'updated_at',
        ])

    @staticmethod
    def add_attribute(product, key, value, sort_order=0):
        attribute = ProductAttribute.objects.create(
            product=product,
            key=key,
            value=value,
            sort_order=sort_order,
        )
        return attribute

    @staticmethod
    def add_image(product, image_url, alt_text=None, sort_order=0, is_primary=False):
        if is_primary:
            ProductImage.objects.filter(product=product, is_primary=True).update(is_primary=False)
        image = ProductImage.objects.create(
            product=product,
            image_url=image_url,
            alt_text=alt_text,
            sort_order=sort_order,
            is_primary=is_primary,
        )
        return image

    @staticmethod
    def add_document(product, title, file_url, file_type, file_size=None):
        document = ProductDocument.objects.create(
            product=product,
            title=title,
            file_url=file_url,
            file_type=file_type,
            file_size=file_size,
        )
        return document
