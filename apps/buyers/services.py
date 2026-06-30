from .models import BuyerProfile, BuyerAddress


class BuyerService:
    @staticmethod
    def get_profile(user):
        try:
            return user.buyer_profile
        except BuyerProfile.DoesNotExist:
            return None

    @staticmethod
    def update_profile(user, data):
        profile, created = BuyerProfile.objects.get_or_create(user=user)
        for field, value in data.items():
            if value is not None:
                setattr(profile, field, value)
        profile.save()
        return profile

    @staticmethod
    def get_addresses(buyer_profile, address_type=None):
        queryset = buyer_profile.addresses.all()
        if address_type:
            queryset = queryset.filter(address_type=address_type)
        return queryset

    @staticmethod
    def create_address(buyer_profile, data):
        address = BuyerAddress(buyer=buyer_profile, **data)
        address.save()
        return address

    @staticmethod
    def update_address(address, data):
        for field, value in data.items():
            if value is not None:
                setattr(address, field, value)
        address.save()
        return address

    @staticmethod
    def delete_address(address_id, buyer_profile):
        try:
            address = BuyerAddress.objects.get(id=address_id, buyer=buyer_profile)
            address.delete()
            return True
        except BuyerAddress.DoesNotExist:
            return False

    @staticmethod
    def set_default_address(address_id, buyer_profile):
        try:
            address = BuyerAddress.objects.get(id=address_id, buyer=buyer_profile)
            address.is_default = True
            address.save()
            return address
        except BuyerAddress.DoesNotExist:
            return None
