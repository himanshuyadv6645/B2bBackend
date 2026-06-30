from rest_framework import generics
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from apps.inventory.models import Inventory, StockHistory
from apps.inventory.serializers.inventory import (
    InventorySerializer,
    InventoryCreateSerializer,
    StockAdjustSerializer,
    StockHistorySerializer,
)
from apps.inventory.services import InventoryService
from apps.sellers.services import SellerService
from common.permissions import IsApprovedSeller
from common.response import success_response, created_response, bad_request_response
from common.pagination import StandardResultsPagination


class SellerInventoryListView(generics.ListAPIView):
    permission_classes = [IsApprovedSeller]
    serializer_class = InventorySerializer
    pagination_class = StandardResultsPagination

    def get_queryset(self):
        profile = SellerService.get_profile(self.request.user)
        variant = self.request.query_params.get('variant')
        return InventoryService.get_inventory(profile, variant)

    @extend_schema(tags=['Inventory'], summary='List your inventory')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class SellerInventoryCreateView(generics.CreateAPIView):
    permission_classes = [IsApprovedSeller]
    serializer_class = InventoryCreateSerializer

    @extend_schema(tags=['Inventory'], summary='Create inventory entry')
    def post(self, request, *args, **kwargs):
        profile = SellerService.get_profile(request.user)
        serializer = InventoryCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        inventory = InventoryService.create_inventory(profile, serializer.validated_data)
        return created_response(data=InventorySerializer(inventory).data, message='Inventory created')


class SellerStockAdjustView(generics.GenericAPIView):
    permission_classes = [IsApprovedSeller]

    @extend_schema(tags=['Inventory'], summary='Adjust stock for an inventory entry')
    def post(self, request, pk):
        profile = SellerService.get_profile(request.user)
        from apps.inventory.models import Inventory
        inventory = Inventory.objects.get(id=pk, seller=profile)

        serializer = StockAdjustSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            inventory = InventoryService.adjust_stock(
                inventory=inventory,
                quantity=serializer.validated_data['quantity'],
                change_type=serializer.validated_data['change_type'],
                notes=serializer.validated_data.get('notes', ''),
                performed_by=request.user,
            )
            return success_response(data=InventorySerializer(inventory).data, message='Stock adjusted')
        except ValueError as e:
            return bad_request_response(message=str(e))


class SellerStockHistoryView(generics.ListAPIView):
    permission_classes = [IsApprovedSeller]
    serializer_class = StockHistorySerializer
    pagination_class = StandardResultsPagination

    def get_queryset(self):
        return StockHistory.objects.filter(
            inventory__seller=SellerService.get_profile(self.request.user)
        )

    @extend_schema(tags=['Inventory'], summary='View stock history')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
