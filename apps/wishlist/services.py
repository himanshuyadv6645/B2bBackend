from apps.wishlist.models import Wishlist


class WishlistService:
    @staticmethod
    def get_wishlist(buyer):
        return Wishlist.objects.filter(buyer=buyer).select_related('variant', 'variant__product')

    @staticmethod
    def add_to_wishlist(buyer, variant_id):
        wishlist, created = Wishlist.objects.get_or_create(
            buyer=buyer,
            variant_id=variant_id,
        )
        return wishlist, created

    @staticmethod
    def remove_from_wishlist(buyer, variant_id):
        deleted, _ = Wishlist.objects.filter(buyer=buyer, variant_id=variant_id).delete()
        return deleted > 0

    @staticmethod
    def is_in_wishlist(buyer, variant_id):
        return Wishlist.objects.filter(buyer=buyer, variant_id=variant_id).exists()
