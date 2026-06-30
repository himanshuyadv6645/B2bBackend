from rest_framework import serializers
from apps.buyers.models import BuyerProfile, BuyerAddress


class BuyerProfileSerializer(serializers.ModelSerializer):
    full_name = serializers.ReadOnlyField()

    class Meta:
        model = BuyerProfile
        fields = [
            'id', 'first_name', 'last_name', 'full_name', 'phone', 'avatar',
            'company_name', 'gstin', 'pan_number', 'business_type',
            'is_verified', 'created_at', 'updated_at',
        ]
        read_only_fields = ['id', 'is_verified', 'created_at', 'updated_at']


class BuyerProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyerProfile
        fields = ['first_name', 'last_name', 'phone', 'company_name', 'gstin', 'pan_number', 'business_type']


class BuyerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyerAddress
        fields = [
            'id', 'address_type', 'label', 'contact_name', 'contact_phone',
            'address_line1', 'address_line2', 'city', 'state', 'pincode',
            'country', 'latitude', 'longitude', 'is_default', 'created_at', 'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_pincode(self, value):
        if not value.isdigit() or len(value) != 6:
            raise serializers.ValidationError('Pincode must be 6 digits.')
        return value

    def validate_contact_phone(self, value):
        if not value.isdigit() or len(value) != 10:
            raise serializers.ValidationError('Phone number must be 10 digits.')
        return value
