from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema

from apps.cart.models import CartItem
from apps.cart.serializers.cart import (
    CartSerializer,
    CartItemSerializer,
    AddToCartSerializer,
    UpdateCartItemSerializer,
)
from apps.cart.services import CartService
from apps.buyers.services import BuyerService
from common.permissions import IsBuyerUser
from common.response import success_response, created_response, not_found_response, bad_request_response


class CartView(generics.RetrieveAPIView):
    permission_classes = [IsBuyerUser]

    @extend_schema(tags=['Cart'], summary='Get cart with items')
    def get(self, request, *args, **kwargs):
        profile = BuyerService.get_profile(request.user)
        if not profile:
            return not_found_response('Complete your profile first')
        cart = CartService.get_cart(profile)
        serializer = CartSerializer(cart)
        return success_response(data=serializer.data)


class AddToCartView(APIView):
    permission_classes = [IsBuyerUser]

    @extend_schema(tags=['Cart'], summary='Add item to cart')
    def post(self, request):
        profile = BuyerService.get_profile(request.user)
        if not profile:
            return not_found_response('Complete your profile first')

        serializer = AddToCartSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            cart_item = CartService.add_to_cart(
                buyer=profile,
                seller_id=serializer.validated_data['seller_id'],
                variant_id=serializer.validated_data['variant_id'],
                quantity=serializer.validated_data['quantity'],
                notes=serializer.validated_data.get('notes', ''),
            )
            return created_response(
                data=CartItemSerializer(cart_item).data,
                message='Item added to cart',
            )
        except ValueError as e:
            return bad_request_response(message=str(e))


class UpdateCartItemView(APIView):
    permission_classes = [IsBuyerUser]

    @extend_schema(tags=['Cart'], summary='Update cart item quantity')
    def patch(self, request, item_id):
        profile = BuyerService.get_profile(request.user)
        serializer = UpdateCartItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            cart_item = CartService.update_cart_item(
                cart_item_id=item_id,
                buyer=profile,
                quantity=serializer.validated_data['quantity'],
            )
            return success_response(
                data=CartItemSerializer(cart_item).data,
                message='Cart item updated',
            )
        except (CartItem.DoesNotExist, ValueError) as e:
            return bad_request_response(message=str(e))


class RemoveFromCartView(APIView):
    permission_classes = [IsBuyerUser]

    @extend_schema(tags=['Cart'], summary='Remove item from cart')
    def delete(self, request, item_id):
        profile = BuyerService.get_profile(request.user)
        CartService.remove_from_cart(item_id, profile)
        return success_response(message='Item removed from cart')


class ClearCartView(APIView):
    permission_classes = [IsBuyerUser]

    @extend_schema(tags=['Cart'], summary='Clear entire cart')
    def delete(self, request):
        profile = BuyerService.get_profile(request.user)
        CartService.clear_cart(profile)
        return success_response(message='Cart cleared')
