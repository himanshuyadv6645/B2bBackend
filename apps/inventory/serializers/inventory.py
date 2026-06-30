from rest_framework import serializers
from apps.inventory.models import Inventory, StockHistory, InventoryLog


class InventorySerializer(serializers.ModelSerializer):
    variant_name = serializers.CharField(source='variant.name', read_only=True)
    seller_name = serializers.CharField(source='seller.company_name', read_only=True)
    warehouse_name = serializers.CharField(source='warehouse.name', read_only=True)
    variant_detail = serializers.SerializerMethodField()
    warehouse_detail = serializers.SerializerMethodField()

    class Meta:
        model = Inventory
        fields = [
            'id', 'seller', 'seller_name', 'variant', 'variant_name', 'variant_detail',
            'warehouse', 'warehouse_name', 'warehouse_detail', 'total_stock', 'reserved_stock',
            'available_stock', 'low_stock_threshold', 'created_at', 'updated_at',
        ]
        read_only_fields = ['id', 'available_stock', 'created_at', 'updated_at']

    def get_variant_detail(self, obj):
        from common.serializer_helpers import build_variant_detail
        return build_variant_detail(obj.variant)

    def get_warehouse_detail(self, obj):
        w = obj.warehouse
        if not w:
            return None
        return {'id': str(w.id), 'name': w.name, 'city': getattr(w, 'city', None)}


class InventoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['variant', 'warehouse', 'total_stock', 'low_stock_threshold']


class StockAdjustSerializer(serializers.Serializer):
    quantity = serializers.IntegerField()
    change_type = serializers.ChoiceField(choices=['add', 'remove', 'adjustment'])
    notes = serializers.CharField(required=False, allow_blank=True)


class StockHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = StockHistory
        fields = [
            'id', 'change_type', 'quantity_change', 'previous_stock',
            'new_stock', 'reference_type', 'reference_id', 'notes', 'created_at',
        ]
