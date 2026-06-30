from rest_framework import serializers
from apps.sellers.models import SellerProfile, SellerWarehouse


class SellerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerProfile
        fields = [
            'id', 'company_name', 'gstin', 'pan_number',
            'contact_name', 'contact_phone', 'logo', 'banner',
            'description', 'business_type', 'website', 'status',
            'approval_date', 'commission_rate', 'rating', 'total_ratings',
            'is_verified', 'created_at', 'updated_at',
        ]
        read_only_fields = [
            'id', 'status', 'approval_date', 'commission_rate',
            'rating', 'total_ratings', 'is_verified', 'created_at', 'updated_at',
        ]


class SellerProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerProfile
        fields = [
            'company_name', 'gstin', 'pan_number',
            'contact_name', 'contact_phone', 'logo', 'banner',
            'description', 'business_type', 'website',
        ]


class SellerWarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerWarehouse
        fields = [
            'id', 'name', 'contact_phone', 'address_line1', 'address_line2',
            'city', 'state', 'pincode', 'country', 'latitude', 'longitude',
            'is_active', 'is_primary', 'created_at', 'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class AdminSellerApprovalSerializer(serializers.Serializer):
    action = serializers.ChoiceField(choices=['approve', 'reject'])
    reason = serializers.CharField(required=False, allow_blank=True)
