"""Shared helpers for building consistent nested detail payloads in serializers."""


def get_product_image(product):
    """Return the primary (or first) product image URL, or None."""
    if not product:
        return None
    img = product.images.filter(is_primary=True).first() or product.images.first()
    return img.image_url if img else None


def get_variant_image(variant):
    """Return the variant's primary image, falling back to the product image."""
    if not variant:
        return None
    img = variant.images.filter(is_primary=True).first() or variant.images.first()
    if img:
        return img.image_url
    if variant.product_id:
        return get_product_image(variant.product)
    return None


def build_variant_detail(variant):
    """Consistent nested variant payload used across pricing/inventory/cart/wishlist."""
    if not variant:
        return None
    product = None
    if variant.product_id:
        product = {
            'id': str(variant.product.id),
            'name': variant.product.name,
            'slug': variant.product.slug,
        }
    selling_price = getattr(variant, 'min_selling_price', None)
    return {
        'id': str(variant.id),
        'name': variant.name,
        'sku': variant.sku,
        'slug': getattr(variant, 'slug', None),
        'selling_price': str(selling_price) if selling_price is not None else None,
        'image': get_variant_image(variant),
        'product': product,
    }
