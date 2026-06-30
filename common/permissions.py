from rest_framework.permissions import BasePermission


class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role == 'admin'
        )


class IsBuyerUser(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role == 'buyer'
        )


class IsSellerUser(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role == 'seller'
        )


class IsApprovedSeller(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role == 'seller'
            and hasattr(request.user, 'seller_profile')
            and request.user.seller_profile.status == 'approved'
        )


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        if hasattr(obj, 'user'):
            return obj.user == request.user
        if hasattr(obj, 'buyer'):
            return obj.buyer.user == request.user
        return False


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role == 'admin'
        )


class IsSellerOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        return obj.seller.user == request.user


class IsAdminOrApprovedSeller(BasePermission):
    """Allow admin (full access) or approved seller to create/update products."""
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        if request.user.role == 'admin':
            return True
        if (request.user.role == 'seller'
                and hasattr(request.user, 'seller_profile')
                and request.user.seller_profile.status == 'approved'):
            return True
        return False
