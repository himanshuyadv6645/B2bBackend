from rest_framework import serializers
from apps.orders.models import Order, OrderItem, SellerOrder, Invoice


class OrderItemSerializer(serializers.ModelSerializer):
    seller_name = serializers.CharField(source='seller.company_name', read_only=True)

    class Meta:
        model = OrderItem
        fields = [
            'id', 'seller', 'seller_name', 'variant', 'product_name',
            'variant_name', 'product_image', 'quantity', 'unit_price',
            'tax_rate', 'tax_amount', 'shipping_charge', 'discount',
            'total_price', 'status',
        ]


class SellerOrderSerializer(serializers.ModelSerializer):
    seller_name = serializers.CharField(source='seller.company_name', read_only=True)
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = SellerOrder
        fields = [
            'id', 'seller', 'seller_name', 'status', 'subtotal',
            'total_tax', 'total_shipping', 'total_amount',
            'tracking_number', 'tracking_url', 'shipped_at',
            'delivered_at', 'items', 'created_at',
        ]


class OrderListSerializer(serializers.ModelSerializer):
    buyer_name = serializers.CharField(source='buyer.full_name', read_only=True)
    item_count = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = [
            'id', 'order_number', 'buyer_name', 'status', 'payment_status',
            'subtotal', 'total_tax', 'total_shipping', 'total_discount',
            'total_amount', 'item_count', 'created_at',
        ]

    def get_item_count(self, obj):
        return obj.items.count()


class OrderDetailSerializer(serializers.ModelSerializer):
    buyer_name = serializers.CharField(source='buyer.full_name', read_only=True)
    items = OrderItemSerializer(many=True, read_only=True)
    seller_orders = SellerOrderSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = [
            'id', 'order_number', 'buyer_name', 'status', 'payment_status',
            'subtotal', 'total_tax', 'total_shipping', 'total_discount',
            'total_amount', 'notes', 'cancellation_reason', 'cancelled_at',
            'delivered_at', 'items', 'seller_orders', 'created_at', 'updated_at',
        ]


class CreateOrderSerializer(serializers.Serializer):
    billing_address_id = serializers.UUIDField()
    shipping_address_id = serializers.UUIDField()
    notes = serializers.CharField(required=False, allow_blank=True)


class InvoiceSerializer(serializers.ModelSerializer):
    seller_name = serializers.CharField(source='seller.company_name', read_only=True)
    buyer_name = serializers.CharField(source='buyer.full_name', read_only=True)

    class Meta:
        model = Invoice
        fields = [
            'id', 'invoice_number', 'seller_name', 'buyer_name',
            'subtotal', 'cgst', 'sgst', 'igst', 'total_tax',
            'total_discount', 'total_amount', 'pdf_url', 'status',
            'issued_at', 'paid_at', 'created_at',
        ]
