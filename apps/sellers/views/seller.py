from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

from apps.sellers.models import SellerProfile, SellerWarehouse
from apps.sellers.serializers.seller import (
    SellerProfileSerializer,
    SellerWarehouseSerializer,
    AdminSellerApprovalSerializer,
)
from apps.sellers.services import SellerService
from common.permissions import IsSellerUser, IsApprovedSeller, IsAdminUser
from common.response import success_response, created_response, not_found_response


class SellerProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, IsSellerUser]

    @extend_schema(tags=['Sellers'], summary='Get seller profile')
    def get(self, request, *args, **kwargs):
        profile = SellerService.get_profile(request.user)
        if not profile:
            return not_found_response('Profile not found')
        serializer = SellerProfileSerializer(profile)
        return success_response(data=serializer.data)

    @extend_schema(tags=['Sellers'], summary='Update seller profile')
    def patch(self, request, *args, **kwargs):
        profile = SellerService.update_profile(request.user, request.data)
        serializer = SellerProfileSerializer(profile)
        return success_response(data=serializer.data, message='Profile updated')


class SellerWarehouseListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsSellerUser]

    def get_serializer_class(self):
        return SellerWarehouseSerializer

    def get_queryset(self):
        profile = SellerService.get_profile(self.request.user)
        if not profile:
            return SellerWarehouse.objects.none()
        return SellerService.get_warehouses(profile)

    @extend_schema(tags=['Sellers'], summary='List seller warehouses')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(tags=['Sellers'], summary='Create seller warehouse')
    def post(self, request, *args, **kwargs):
        profile = SellerService.get_profile(request.user)
        if not profile:
            return not_found_response('Complete your seller profile first')

        serializer = SellerWarehouseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        warehouse = SellerService.create_warehouse(profile, serializer.validated_data)
        return created_response(data=SellerWarehouseSerializer(warehouse).data, message='Warehouse created')


class SellerWarehouseDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsSellerUser]
    serializer_class = SellerWarehouseSerializer

    def get_object(self):
        profile = SellerService.get_profile(self.request.user)
        return SellerWarehouse.objects.get(id=self.kwargs['pk'], seller=profile)

    @extend_schema(tags=['Sellers'], summary='Get warehouse details')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(tags=['Sellers'], summary='Update warehouse')
    def patch(self, request, *args, **kwargs):
        warehouse = self.get_object()
        warehouse = SellerService.update_warehouse(warehouse, request.data)
        return success_response(data=SellerWarehouseSerializer(warehouse).data, message='Warehouse updated')

    @extend_schema(tags=['Sellers'], summary='Delete warehouse')
    def delete(self, request, *args, **kwargs):
        profile = SellerService.get_profile(self.request.user)
        SellerService.delete_warehouse(self.kwargs['pk'], profile)
        return success_response(message='Warehouse deleted')


class AdminSellerListView(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = SellerProfileSerializer

    def get_queryset(self):
        queryset = SellerProfile.objects.all()
        status_filter = self.request.query_params.get('status')
        search = self.request.query_params.get('search')

        if status_filter:
            queryset = queryset.filter(status=status_filter)
        if search:
            queryset = queryset.filter(company_name__icontains=search)
        return queryset

    @extend_schema(tags=['Sellers'], summary='Admin: List all sellers')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class AdminSellerApproveView(generics.GenericAPIView):
    permission_classes = [IsAdminUser]
    queryset = SellerProfile.objects.all()

    @extend_schema(tags=['Sellers'], summary='Admin: Approve or reject seller')
    def post(self, request, pk):
        seller = self.get_object()
        serializer = AdminSellerApprovalSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        action = serializer.validated_data['action']
        reason = serializer.validated_data.get('reason', '')

        if action == 'approve':
            seller = SellerService.approve_seller(seller)
            message = 'Seller approved'
        else:
            seller = SellerService.reject_seller(seller, reason)
            message = 'Seller rejected'

        return success_response(data=SellerProfileSerializer(seller).data, message=message)
