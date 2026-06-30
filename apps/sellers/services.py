from django.utils import timezone
from apps.sellers.models import SellerProfile, SellerWarehouse


class SellerService:
    @staticmethod
    def get_profile(user):
        try:
            return user.seller_profile
        except SellerProfile.DoesNotExist:
            return None

    @staticmethod
    def update_profile(user, data):
        profile, created = SellerProfile.objects.get_or_create(user=user)
        for field, value in data.items():
            if value is not None:
                setattr(profile, field, value)
        profile.save()
        return profile

    @staticmethod
    def approve_seller(seller_profile):
        seller_profile.status = 'approved'
        seller_profile.approval_date = timezone.now()
        seller_profile.save(update_fields=['status', 'approval_date', 'updated_at'])
        return seller_profile

    @staticmethod
    def reject_seller(seller_profile, reason=''):
        seller_profile.status = 'rejected'
        seller_profile.rejection_reason = reason
        seller_profile.save(update_fields=['status', 'rejection_reason', 'updated_at'])
        return seller_profile

    @staticmethod
    def suspend_seller(seller_profile):
        seller_profile.status = 'suspended'
        seller_profile.save(update_fields=['status', 'updated_at'])
        return seller_profile

    @staticmethod
    def get_warehouses(seller_profile):
        return seller_profile.warehouses.all()

    @staticmethod
    def create_warehouse(seller_profile, data):
        warehouse = SellerWarehouse(seller=seller_profile, **data)
        warehouse.save()
        return warehouse

    @staticmethod
    def update_warehouse(warehouse, data):
        for field, value in data.items():
            if value is not None:
                setattr(warehouse, field, value)
        warehouse.save()
        return warehouse

    @staticmethod
    def delete_warehouse(warehouse_id, seller_profile):
        try:
            warehouse = SellerWarehouse.objects.get(id=warehouse_id, seller=seller_profile)
            warehouse.delete()
            return True
        except SellerWarehouse.DoesNotExist:
            return False
