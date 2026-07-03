from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from apps.reviews.models import ProductReview, SellerReview
from apps.reviews.serializers.review import ProductReviewSerializer, SellerReviewSerializer
from apps.reviews.services import ReviewService
from common.permissions import IsAdminUser
from common.response import success_response, bad_request_response, not_found_response
from common.pagination import StandardResultsPagination


class AdminProductReviewListView(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ProductReviewSerializer
    pagination_class = StandardResultsPagination

    def get_queryset(self):
        queryset = ProductReview.objects.all().order_by('-created_at')
        status = self.request.query_params.get('status')
        if status:
            queryset = queryset.filter(status=status)
        return queryset

    @extend_schema(tags=['Admin Reviews'], summary='Admin: List product reviews')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class AdminSellerReviewListView(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = SellerReviewSerializer
    pagination_class = StandardResultsPagination

    def get_queryset(self):
        queryset = SellerReview.objects.all().order_by('-created_at')
        status = self.request.query_params.get('status')
        if status:
            queryset = queryset.filter(status=status)
        return queryset

    @extend_schema(tags=['Admin Reviews'], summary='Admin: List seller reviews')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class AdminApproveProductReviewView(APIView):
    permission_classes = [IsAdminUser]

    @extend_schema(tags=['Admin Reviews'], summary='Admin: Approve product review')
    def post(self, request, pk):
        try:
            review = ReviewService.approve_product_review(pk)
            return success_response(data=ProductReviewSerializer(review).data, message='Review approved')
        except ProductReview.DoesNotExist:
            return not_found_response('Review not found')


class AdminRejectProductReviewView(APIView):
    permission_classes = [IsAdminUser]

    @extend_schema(tags=['Admin Reviews'], summary='Admin: Reject product review')
    def post(self, request, pk):
        try:
            review = ReviewService.reject_product_review(pk)
            return success_response(data=ProductReviewSerializer(review).data, message='Review rejected')
        except ProductReview.DoesNotExist:
            return not_found_response('Review not found')


class AdminApproveSellerReviewView(APIView):
    permission_classes = [IsAdminUser]

    @extend_schema(tags=['Admin Reviews'], summary='Admin: Approve seller review')
    def post(self, request, pk):
        try:
            review = ReviewService.approve_seller_review(pk)
            return success_response(data=SellerReviewSerializer(review).data, message='Review approved')
        except SellerReview.DoesNotExist:
            return not_found_response('Review not found')


class AdminRejectSellerReviewView(APIView):
    permission_classes = [IsAdminUser]

    @extend_schema(tags=['Admin Reviews'], summary='Admin: Reject seller review')
    def post(self, request, pk):
        try:
            review = ReviewService.reject_seller_review(pk)
            return success_response(data=SellerReviewSerializer(review).data, message='Review rejected')
        except SellerReview.DoesNotExist:
            return not_found_response('Review not found')
