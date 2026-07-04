from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from apps.dashboard.services import DashboardService
from apps.buyers.services import BuyerService
from apps.sellers.services import SellerService
from apps.orders.models import Order
from apps.orders.serializers.order import OrderListSerializer
from common.permissions import IsBuyerUser, IsSellerUser, IsAdminUser
from common.response import success_response
from common.pagination import StandardResultsPagination


class BuyerDashboardView(APIView):
    permission_classes = [IsBuyerUser]

    @extend_schema(tags=['Dashboard'], summary='Buyer dashboard stats')
    def get(self, request):
        profile = BuyerService.get_profile(request.user)
        data = DashboardService.get_buyer_dashboard(profile)
        data['recent_orders'] = OrderListSerializer(data['recent_orders'], many=True).data
        return success_response(data=data)


class DashboardSellerRecentOrderSerializer(serializers.ModelSerializer):
    order_number = serializers.CharField(source='order.order_number', read_only=True)
    buyer_name = serializers.CharField(source='order.buyer.full_name', read_only=True)

    class Meta:
        from apps.orders.models import SellerOrder
        model = SellerOrder
        fields = ['id', 'order_number', 'buyer_name', 'status', 'total_amount', 'created_at']

class SellerDashboardView(APIView):
    permission_classes = [IsSellerUser]

    @extend_schema(tags=['Dashboard'], summary='Seller dashboard stats')
    def get(self, request):
        profile = SellerService.get_profile(request.user)
        data = DashboardService.get_seller_dashboard(profile)
        data['recent_orders'] = DashboardSellerRecentOrderSerializer(data['recent_orders'], many=True).data
        return success_response(data=data)


class AdminDashboardView(APIView):
    permission_classes = [IsAdminUser]

    @extend_schema(tags=['Dashboard'], summary='Admin dashboard stats')
    def get(self, request):
        data = DashboardService.get_admin_dashboard()
        data['recent_orders'] = OrderListSerializer(data['recent_orders'], many=True).data
        return success_response(data=data)
