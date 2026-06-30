from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema

from apps.orders.models import Order, SellerOrder, Invoice
from apps.orders.serializers.order import (
    OrderListSerializer,
    OrderDetailSerializer,
    CreateOrderSerializer,
    SellerOrderSerializer,
    InvoiceSerializer,
)
from apps.orders.services import OrderService
from apps.buyers.services import BuyerService
from apps.sellers.services import SellerService
from common.permissions import IsBuyerUser, IsSellerUser, IsAdminUser
from common.response import success_response, created_response, bad_request_response, not_found_response
from common.pagination import StandardResultsPagination


class BuyerOrderListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsBuyerUser]
    pagination_class = StandardResultsPagination

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateOrderSerializer
        return OrderListSerializer

    def get_queryset(self):
        profile = BuyerService.get_profile(self.request.user)
        status_filter = self.request.query_params.get('status')
        return OrderService.get_buyer_orders(profile, status_filter)

    @extend_schema(tags=['Orders'], summary='List your orders')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(tags=['Orders'], summary='Create order from cart')
    def post(self, request, *args, **kwargs):
        profile = BuyerService.get_profile(request.user)
        if not profile:
            return not_found_response('Complete your profile first')

        serializer = CreateOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            order = OrderService.create_order(
                buyer=profile,
                billing_address_id=serializer.validated_data['billing_address_id'],
                shipping_address_id=serializer.validated_data['shipping_address_id'],
                notes=serializer.validated_data.get('notes', ''),
            )
            return created_response(
                data=OrderDetailSerializer(order).data,
                message='Order placed successfully',
            )
        except ValueError as e:
            return bad_request_response(message=str(e))


class BuyerOrderDetailView(generics.RetrieveAPIView):
    permission_classes = [IsBuyerUser]
    serializer_class = OrderDetailSerializer

    def get_object(self):
        profile = BuyerService.get_profile(self.request.user)
        return Order.objects.get(
            order_number=self.kwargs['order_number'],
            buyer=profile,
            deleted_at__isnull=True,
        )

    @extend_schema(tags=['Orders'], summary='Get order details')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class BuyerCancelOrderView(APIView):
    permission_classes = [IsBuyerUser]

    @extend_schema(tags=['Orders'], summary='Cancel order')
    def post(self, request, order_number):
        profile = BuyerService.get_profile(request.user)
        try:
            order = Order.objects.get(order_number=order_number, buyer=profile)
            reason = request.data.get('reason', '')
            order = OrderService.cancel_order(order, reason)
            return success_response(
                data=OrderDetailSerializer(order).data,
                message='Order cancelled',
            )
        except Order.DoesNotExist:
            return not_found_response('Order not found')


class SellerOrderListView(generics.ListAPIView):
    permission_classes = [IsSellerUser]
    serializer_class = SellerOrderSerializer
    pagination_class = StandardResultsPagination

    def get_queryset(self):
        profile = SellerService.get_profile(self.request.user)
        status_filter = self.request.query_params.get('status')
        return OrderService.get_seller_orders(profile, status_filter)

    @extend_schema(tags=['Orders'], summary='List seller orders')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class SellerOrderDetailView(generics.RetrieveAPIView):
    permission_classes = [IsSellerUser]
    serializer_class = SellerOrderSerializer

    def get_object(self):
        profile = SellerService.get_profile(self.request.user)
        return SellerOrder.objects.get(id=self.kwargs['pk'], seller=profile)

    @extend_schema(tags=['Orders'], summary='Get seller order details')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class SellerShipOrderView(APIView):
    permission_classes = [IsSellerUser]

    @extend_schema(tags=['Orders'], summary='Seller: Ship order')
    def post(self, request, pk):
        profile = SellerService.get_profile(self.request.user)
        try:
            seller_order = SellerOrder.objects.get(id=pk, seller=profile)
            tracking_number = request.data.get('tracking_number')
            tracking_url = request.data.get('tracking_url')
            seller_order = OrderService.ship_order(seller_order, tracking_number, tracking_url)
            return success_response(
                data=SellerOrderSerializer(seller_order).data,
                message='Order shipped',
            )
        except SellerOrder.DoesNotExist:
            return not_found_response('Order not found')


class SellerDeliverOrderView(APIView):
    permission_classes = [IsSellerUser]

    @extend_schema(tags=['Orders'], summary='Seller: Mark order as delivered')
    def post(self, request, pk):
        profile = SellerService.get_profile(self.request.user)
        try:
            seller_order = SellerOrder.objects.get(id=pk, seller=profile)
            seller_order = OrderService.deliver_order(seller_order)
            return success_response(
                data=SellerOrderSerializer(seller_order).data,
                message='Order delivered',
            )
        except SellerOrder.DoesNotExist:
            return not_found_response('Order not found')


class InvoiceListView(generics.ListAPIView):
    permission_classes = [IsBuyerUser]
    serializer_class = InvoiceSerializer
    pagination_class = StandardResultsPagination

    def get_queryset(self):
        profile = BuyerService.get_profile(self.request.user)
        return Invoice.objects.filter(buyer=profile)

    @extend_schema(tags=['Orders'], summary='List your invoices')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class InvoiceDetailView(generics.RetrieveAPIView):
    permission_classes = [IsBuyerUser]
    serializer_class = InvoiceSerializer

    def get_object(self):
        profile = BuyerService.get_profile(self.request.user)
        return Invoice.objects.get(id=self.kwargs['pk'], buyer=profile)

    @extend_schema(tags=['Orders'], summary='Get invoice details')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
