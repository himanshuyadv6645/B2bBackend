from rest_framework import generics, status
from rest_framework.permissions import BasePermission
from drf_spectacular.utils import extend_schema

from apps.products.models import Product, ProductImage
from apps.products.serializers.product import ProductImageSerializer
from common.response import success_response, created_response, bad_request_response, not_found_response, forbidden_response


class IsAdminOrSellerOwner(BasePermission):
    """Admin can manage any product images; seller can manage their own products."""
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

    def has_object_permission(self, request, view, obj):
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        if request.user.role == 'admin':
            return True
        # Seller can only manage images for their own products
        product = obj if isinstance(obj, Product) else obj.product
        return product.seller == request.user.seller_profile


class ProductImageListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrSellerOwner]
    serializer_class = ProductImageSerializer

    def get_queryset(self):
        product_id = self.kwargs.get('product_pk')
        return ProductImage.objects.filter(product_id=product_id).order_by('sort_order')

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['product_id'] = self.kwargs.get('product_pk')
        return context

    @extend_schema(tags=['Product Images'], summary='List product images')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(tags=['Product Images'], summary='Upload product image')
    def post(self, request, *args, **kwargs):
        product_id = self.kwargs.get('product_pk')
        try:
            product = Product.all_objects.get(id=product_id)
        except Product.DoesNotExist:
            return not_found_response(message='Product not found')

        # Check permission on the product
        if not self.check_object_permissions(request, product):
            return forbidden_response(message='Permission denied')

        image_file = request.FILES.get('image')
        if not image_file:
            return bad_request_response(message='No image file provided')

        # Upload to Cloudinary
        from utils.file_upload import upload_image
        folder = f'b2bmarketplace/products/{product_id}'
        result = upload_image(image_file, folder=folder)

        if 'error' in result:
            return bad_request_response(message=f'Upload failed: {result["error"]}')

        # If this is marked as primary, unset other primary images
        is_primary = request.data.get('is_primary', 'false').lower() == 'true'
        if is_primary:
            ProductImage.objects.filter(product=product, is_primary=True).update(is_primary=False)

        # Determine sort order
        existing_count = ProductImage.objects.filter(product=product).count()
        sort_order = int(request.data.get('sort_order', existing_count))

        image = ProductImage.objects.create(
            product=product,
            image_url=result['url'],
            alt_text=request.data.get('alt_text', ''),
            sort_order=sort_order,
            is_primary=is_primary,
        )

        serializer = ProductImageSerializer(image)
        return created_response(data=serializer.data)


class ProductImageDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAdminOrSellerOwner]
    serializer_class = ProductImageSerializer

    def get_queryset(self):
        product_id = self.kwargs.get('product_pk')
        return ProductImage.objects.filter(product_id=product_id)

    @extend_schema(tags=['Product Images'], summary='Delete product image')
    def delete(self, request, *args, **kwargs):
        image = self.get_object()
        product = image.product

        if not self.check_object_permissions(request, product):
            return forbidden_response(message='Permission denied')

        # Delete from Cloudinary
        # Extract public_id from URL if possible
        image.delete()

        return success_response(message='Image deleted')
