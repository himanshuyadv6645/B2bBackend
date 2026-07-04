from apps.pricing.models import SellerPricing, WholesaleTier
from apps.products.services import ProductService


class PricingService:
    @staticmethod
    def get_pricing_for_variant(variant_id, seller_id=None):
        queryset = SellerPricing.objects.filter(
            variant_id=variant_id, is_active=True
        ).prefetch_related('wholesale_tiers')
        if seller_id:
            queryset = queryset.filter(seller_id=seller_id)
        return queryset

    @staticmethod
    def get_cheapest_seller(variant_id, quantity=1):
        pricing_list = SellerPricing.objects.filter(
            variant_id=variant_id, is_active=True
        ).prefetch_related('wholesale_tiers')

        best = None
        best_price = None

        for pricing in pricing_list:
            price = pricing.get_wholesale_price(quantity)
            if price is None:
                price = pricing.offer_price if pricing.offer_price is not None else pricing.selling_price

            if best_price is None or price < best_price:
                best_price = price
                best = pricing

        return best

    @staticmethod
    def get_price_for_quantity(pricing, quantity):
        wholesale_price = pricing.get_wholesale_price(quantity)
        if wholesale_price is not None:
            return wholesale_price
        if pricing.offer_price is not None:
            return pricing.offer_price
        return pricing.selling_price

    @staticmethod
    def create_pricing(seller, data):
        pricing = SellerPricing(seller=seller, **data)
        pricing.save()
        ProductService.update_product_stats(pricing.variant.product_id)
        return pricing

    @staticmethod
    def update_pricing(pricing, data):
        for field, value in data.items():
            if value is not None:
                setattr(pricing, field, value)
        pricing.save()
        ProductService.update_product_stats(pricing.variant.product_id)
        return pricing

    @staticmethod
    def add_wholesale_tier(pricing, data):
        tier, created = WholesaleTier.objects.get_or_create(
            pricing=pricing,
            min_quantity=data['min_quantity'],
            defaults={
                'max_quantity': data.get('max_quantity'),
                'price_per_unit': data['price_per_unit'],
                'discount_percent': data.get('discount_percent', 0),
                'notes': data.get('notes', ''),
            },
        )
        if not created:
            tier.max_quantity = data.get('max_quantity', tier.max_quantity)
            tier.price_per_unit = data['price_per_unit']
            tier.discount_percent = data.get('discount_percent', tier.discount_percent)
            tier.notes = data.get('notes', tier.notes)
            tier.save()
        return tier

    @staticmethod
    def remove_wholesale_tier(tier_id, pricing):
        deleted, _ = WholesaleTier.objects.filter(id=tier_id, pricing=pricing).delete()
        return deleted > 0

    @staticmethod
    def get_effective_price(seller_id, variant_id, quantity=1):
        try:
            pricing = SellerPricing.objects.get(
                seller_id=seller_id,
                variant_id=variant_id,
                is_active=True,
            )
            return PricingService.get_price_for_quantity(pricing, quantity)
        except SellerPricing.DoesNotExist:
            return None
