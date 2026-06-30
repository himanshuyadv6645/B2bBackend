from rest_framework import serializers


class BuyerDashboardSerializer(serializers.Serializer):
    total_orders = serializers.IntegerField()
    total_spent = serializers.FloatField()
    recent_orders = serializers.ListField(child=serializers.DictField(), required=False)
    wishlist_count = serializers.IntegerField()
    cart_count = serializers.IntegerField()


class SellerDashboardSerializer(serializers.Serializer):
    total_orders = serializers.IntegerField()
    total_revenue = serializers.FloatField()
    recent_orders = serializers.ListField(child=serializers.DictField(), required=False)
    product_count = serializers.IntegerField()


class AdminDashboardSerializer(serializers.Serializer):
    total_users = serializers.IntegerField()
    total_buyers = serializers.IntegerField()
    total_sellers = serializers.IntegerField()
    pending_sellers = serializers.IntegerField()
    total_orders = serializers.IntegerField()
    total_revenue = serializers.FloatField()
    total_products = serializers.IntegerField()
    recent_orders = serializers.ListField(child=serializers.DictField(), required=False)
