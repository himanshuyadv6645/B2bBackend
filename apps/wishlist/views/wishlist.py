from rest_framework import generics
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from apps.wishlist.models import Wishlist
from apps.wishlist.serializers.wishlist import WishlistSerializer
from apps.wishlist.services import WishlistService
from apps.buyers.services import BuyerService
from common.permissions import IsBuyerUser
from common.response import success_response, created_response, not_found_response


class WishlistListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsBuyerUser]
    serializer_class = WishlistSerializer

    def get_queryset(self):
        profile = BuyerService.get_profile(self.request.user)
        if not profile:
            return Wishlist.objects.none()
        return WishlistService.get_wishlist(profile)

    @extend_schema(tags=['Wishlist'], summary='List wishlist items')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(tags=['Wishlist'], summary='Add item to wishlist')
    def post(self, request, *args, **kwargs):
        profile = BuyerService.get_profile(request.user)
        if not profile:
            return not_found_response('Complete your profile first')

        variant_id = request.data.get('variant_id')
        if not variant_id:
            return not_found_response('variant_id is required')

        wishlist, created = WishlistService.add_to_wishlist(profile, variant_id)
        if created:
            return created_response(message='Added to wishlist')
        return success_response(message='Already in wishlist')


class WishlistDeleteView(generics.DestroyAPIView):
    permission_classes = [IsBuyerUser]

    @extend_schema(tags=['Wishlist'], summary='Remove item from wishlist')
    def delete(self, request, pk):
        profile = BuyerService.get_profile(request.user)
        WishlistService.remove_from_wishlist(profile, pk)
        return success_response(message='Removed from wishlist')
