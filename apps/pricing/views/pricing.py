from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from apps.pricing.models import SellerPricing, WholesaleTier
from apps.pricing.serializers.pricing import (
    SellerPricingSerializer,
    SellerPricingCreateSerializer,
    WholesaleTierSerializer,
    WholesaleTierCreateSerializer,
    BuyerPricingViewSerializer,
)
from apps.pricing.services import PricingService
from apps.sellers.services import SellerService
from common.permissions import IsApprovedSeller
from common.response import success_response, created_response, not_found_response, bad_request_response
from common.pagination import StandardResultsPagination


class SellerPricingListView(generics.ListAPIView):
    permission_classes = [IsApprovedSeller]
    serializer_class = SellerPricingSerializer
    pagination_class = StandardResultsPagination

    def get_queryset(self):
        profile = SellerService.get_profile(self.request.user)
        variant_id = self.request.query_params.get('variant')
        if variant_id:
            return PricingService.get_pricing_for_variant(variant_id, profile.id)
        return SellerPricing.objects.filter(seller=profile).select_related(
            'variant__product', 'warehouse', 'seller'
        ).prefetch_related('wholesale_tiers', 'variant__images', 'variant__product__images')

    @extend_schema(tags=['Pricing'], summary='List your pricing entries with wholesale tiers')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class SellerPricingCreateView(generics.CreateAPIView):
    permission_classes = [IsApprovedSeller]
    serializer_class = SellerPricingCreateSerializer

    @extend_schema(tags=['Pricing'], summary='Create pricing for a variant')
    def post(self, request, *args, **kwargs):
        profile = SellerService.get_profile(request.user)
        serializer = SellerPricingCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        pricing = PricingService.create_pricing(profile, serializer.validated_data)
        return created_response(data=SellerPricingSerializer(pricing).data, message='Pricing created')


class SellerPricingUpdateView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsApprovedSeller]
    serializer_class = SellerPricingCreateSerializer

    def get_queryset(self):
        profile = SellerService.get_profile(self.request.user)
        return SellerPricing.objects.filter(seller=profile)

    @extend_schema(tags=['Pricing'], summary='Update pricing')
    def patch(self, request, *args, **kwargs):
        pricing = self.get_object()
        pricing = PricingService.update_pricing(pricing, request.data)
        return success_response(data=SellerPricingSerializer(pricing).data, message='Pricing updated')

    @extend_schema(tags=['Pricing'], summary='Delete pricing')
    def delete(self, request, *args, **kwargs):
        pricing = self.get_object()
        pricing.delete()
        return success_response(message='Pricing deleted')


class WholesaleTierListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsApprovedSeller]
    serializer_class = WholesaleTierSerializer

    def get_queryset(self):
        pricing = SellerPricing.objects.get(
            id=self.kwargs['pricing_pk'],
            seller=SellerService.get_profile(self.request.user),
        )
        return pricing.wholesale_tiers.all()

    @extend_schema(tags=['Pricing'], summary='List wholesale tiers for a pricing entry')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(tags=['Pricing'], summary='Add wholesale tier (e.g., 1-20 units = Rs.1200, 21-40 = Rs.500)')
    def post(self, request, *args, **kwargs):
        pricing = SellerPricing.objects.get(
            id=self.kwargs['pricing_pk'],
            seller=SellerService.get_profile(self.request.user),
        )
        serializer = WholesaleTierCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tier = PricingService.add_wholesale_tier(pricing, serializer.validated_data)
        return created_response(data=WholesaleTierSerializer(tier).data, message='Tier added')


class WholesaleTierDeleteView(APIView):
    permission_classes = [IsApprovedSeller]

    @extend_schema(tags=['Pricing'], summary='Delete a wholesale tier')
    def delete(self, request, pricing_pk, tier_pk):
        profile = SellerService.get_profile(self.request.user)
        pricing = SellerPricing.objects.get(id=pricing_pk, seller=profile)
        PricingService.remove_wholesale_tier(tier_pk, pricing)
        return success_response(message='Tier deleted')


class CompareSellersView(generics.GenericAPIView):
    permission_classes = []

    @extend_schema(tags=['Pricing'], summary='Compare sellers for a variant with tier pricing')
    def get(self, request, variant_id):
        quantity = int(request.query_params.get('quantity', 1))
        pricing_list = SellerPricing.objects.filter(
            variant_id=variant_id, is_active=True
        ).select_related('seller', 'warehouse').prefetch_related('wholesale_tiers')

        results = []
        for pricing in pricing_list:
            price = PricingService.get_price_for_quantity(pricing, quantity)
            results.append({
                'id': str(pricing.id),
                'seller': str(pricing.seller_id),
                'variant': str(pricing.variant_id),
                'seller_name': pricing.seller.company_name,
                'seller_rating': str(pricing.seller.rating),
                'selling_price': str(pricing.selling_price),
                'effective_price': str(price),
                'offer_price': str(pricing.offer_price) if pricing.offer_price else None,
                'tax_rate': str(pricing.tax_rate),
                'shipping_charge': str(pricing.shipping_charge),
                'free_shipping': pricing.free_shipping,
                'minimum_order_quantity': pricing.minimum_order_quantity,
                'warranty_period': pricing.warranty_period,
                'delivery_time_days': pricing.delivery_time_days,
                'wholesale_tiers': WholesaleTierSerializer(pricing.wholesale_tiers.all(), many=True).data,
            })

        results.sort(key=lambda x: float(x['effective_price']))
        return success_response(data=results)
