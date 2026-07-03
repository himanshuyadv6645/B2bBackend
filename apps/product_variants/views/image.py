from rest_framework import generics
from drf_spectacular.utils import extend_schema

from apps.product_variants.models import ProductVariant, VariantImage
from apps.product_variants.serializers.variant import VariantImageSerializer
from common.permissions import IsAdminOrApprovedSeller
from common.response import success_response, created_response, bad_request_response, not_found_response


class VariantImageListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrApprovedSeller]
    serializer_class = VariantImageSerializer

    def get_queryset(self):
        variant_id = self.kwargs.get('variant_pk')
        return VariantImage.objects.filter(variant_id=variant_id).order_by('sort_order')

    @extend_schema(tags=['Variant Images'], summary='List variant images')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(tags=['Variant Images'], summary='Upload variant image')
    def post(self, request, *args, **kwargs):
        variant_id = self.kwargs.get('variant_pk')
        try:
            variant = ProductVariant.all_objects.get(id=variant_id)
        except ProductVariant.DoesNotExist:
            return not_found_response(message='Variant not found')

        if request.user.role == 'seller':
            from apps.sellers.services import SellerService
            profile = SellerService.get_profile(request.user)
            if variant.product.seller != profile:
                return forbidden_response(message='You do not have permission to modify this variant')

        image_file = request.FILES.get('image')
        if not image_file:
            return bad_request_response(message='No image file provided')

        # Upload to Cloudinary
        from utils.file_upload import upload_image
        folder = f'b2bmarketplace/variants/{variant_id}'
        result = upload_image(image_file, folder=folder)

        if 'error' in result:
            return bad_request_response(message=f'Upload failed: {result["error"]}')

        is_primary = request.data.get('is_primary', 'false').lower() == 'true'
        if is_primary:
            VariantImage.objects.filter(variant=variant, is_primary=True).update(is_primary=False)

        existing_count = VariantImage.objects.filter(variant=variant).count()
        sort_order = int(request.data.get('sort_order', existing_count))

        image = VariantImage.objects.create(
            variant=variant,
            image_url=result['url'],
            alt_text=request.data.get('alt_text', ''),
            sort_order=sort_order,
            is_primary=is_primary,
        )

        serializer = VariantImageSerializer(image)
        return created_response(data=serializer.data)


class VariantImageDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAdminOrApprovedSeller]
    serializer_class = VariantImageSerializer

    def get_queryset(self):
        variant_id = self.kwargs.get('variant_pk')
        return VariantImage.objects.filter(variant_id=variant_id)

    @extend_schema(tags=['Variant Images'], summary='Delete variant image')
    def delete(self, request, *args, **kwargs):
        image = self.get_object()

        if request.user.role == 'seller':
            from apps.sellers.services import SellerService
            profile = SellerService.get_profile(request.user)
            if image.variant.product.seller != profile:
                return forbidden_response(message='You do not have permission to modify this variant')

        image.delete()
        return success_response(message='Image deleted')
