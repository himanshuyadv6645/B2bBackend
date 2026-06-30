from rest_framework import generics
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from apps.reviews.models import ProductReview, SellerReview
from apps.reviews.serializers.review import (
    ProductReviewSerializer,
    ProductReviewCreateSerializer,
    SellerReviewSerializer,
)
from apps.reviews.services import ReviewService
from apps.buyers.services import BuyerService
from common.permissions import IsBuyerUser
from common.response import success_response, created_response, bad_request_response
from common.pagination import StandardResultsPagination


class ProductReviewListCreateView(generics.ListCreateAPIView):
    permission_classes = []
    pagination_class = StandardResultsPagination

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProductReviewCreateSerializer
        return ProductReviewSerializer

    def get_queryset(self):
        product_id = self.request.query_params.get('product')
        if product_id:
            return ReviewService.get_product_reviews(product_id)
        return ProductReview.objects.filter(is_active=True)

    @extend_schema(tags=['Reviews'], summary='List product reviews')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(tags=['Reviews'], summary='Create product review')
    def post(self, request, *args, **kwargs):
        profile = BuyerService.get_profile(request.user)
        if not profile:
            return bad_request_response('Complete your profile first')

        serializer = ProductReviewCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            review = ReviewService.create_product_review(profile, serializer.validated_data)
            return created_response(
                data=ProductReviewSerializer(review).data,
                message='Review created',
            )
        except ValueError as e:
            return bad_request_response(message=str(e))


class SellerReviewListCreateView(generics.ListCreateAPIView):
    permission_classes = []
    pagination_class = StandardResultsPagination

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return SellerReviewSerializer
        return SellerReviewSerializer

    def get_queryset(self):
        seller_id = self.request.query_params.get('seller')
        if seller_id:
            return ReviewService.get_seller_reviews(seller_id)
        return SellerReview.objects.filter(is_active=True)

    @extend_schema(tags=['Reviews'], summary='List seller reviews')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(tags=['Reviews'], summary='Create seller review')
    def post(self, request, *args, **kwargs):
        profile = BuyerService.get_profile(request.user)
        if not profile:
            return bad_request_response('Complete your profile first')

        serializer = SellerReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            reviews = ReviewService.create_seller_review(profile, serializer.validated_data)
            return created_response(
                data=SellerReviewSerializer(reviews, many=True).data,
                message='Review created',
            )
        except ValueError as e:
            return bad_request_response(message=str(e))
