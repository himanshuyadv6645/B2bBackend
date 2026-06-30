from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

from apps.authentication.models import User
from apps.users.serializers.user import (
    UserSerializer,
    ChangePasswordSerializer,
    UpdateProfileSerializer,
    AdminUserListSerializer,
    AdminUserUpdateSerializer,
)
from apps.users.services import UserService
from common.response import success_response, bad_request_response, not_found_response
from common.permissions import IsAdminUser
from common.pagination import StandardResultsPagination


class ProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(tags=['Users'], summary='Get your profile')
    def get(self, request, *args, **kwargs):
        serializer = UserSerializer(request.user)
        return success_response(data=serializer.data)

    @extend_schema(tags=['Users'], summary='Update your profile')
    def patch(self, request, *args, **kwargs):
        serializer = UpdateProfileSerializer(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return success_response(data=UserSerializer(request.user).data, message='Profile updated')


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(tags=['Users'], summary='Change your password')
    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        UserService.change_password(
            user=request.user,
            old_password=serializer.validated_data['old_password'],
            new_password=serializer.validated_data['new_password'],
        )
        return success_response(message='Password changed successfully')


class AdminUserListView(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = AdminUserListSerializer
    pagination_class = StandardResultsPagination

    def get_queryset(self):
        queryset = User.objects.all().order_by('-created_at')
        role = self.request.query_params.get('role')
        is_active = self.request.query_params.get('is_active')
        search = self.request.query_params.get('search')

        if role:
            queryset = queryset.filter(role=role)
        if is_active is not None:
            queryset = queryset.filter(is_active=is_active.lower() == 'true')
        if search:
            queryset = queryset.filter(email__icontains=search) | queryset.filter(phone__icontains=search)

        return queryset

    @extend_schema(tags=['Users'], summary='Admin: List all users')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class AdminUserDetailView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = AdminUserListSerializer

    @extend_schema(tags=['Users'], summary='Admin: Get user details')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(tags=['Users'], summary='Admin: Update user')
    def patch(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = AdminUserUpdateSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return success_response(data=AdminUserListSerializer(user).data, message='User updated')


class AdminToggleUserStatusView(APIView):
    permission_classes = [IsAdminUser]

    @extend_schema(tags=['Users'], summary='Admin: Toggle user active status')
    def post(self, request, user_id):
        try:
            user = UserService.toggle_user_status(user_id)
            return success_response(
                data=AdminUserListSerializer(user).data,
                message=f'User {"activated" if user.is_active else "deactivated"}',
            )
        except User.DoesNotExist:
            return not_found_response('User not found')
