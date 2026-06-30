from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from drf_spectacular.utils import extend_schema

from apps.authentication.services import AuthService
from apps.authentication.serializers.register import (
    RegisterSerializer,
    LoginSerializer,
    RefreshTokenSerializer,
    LogoutSerializer,
)
from common.response import success_response, created_response, bad_request_response, unauthorized_response


class RegisterView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        tags=['Authentication'],
        summary='Register a new user',
        description='Register as a buyer or seller.',
    )
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            user = AuthService.register(
                email=serializer.validated_data['email'],
                password=serializer.validated_data['password'],
                role=serializer.validated_data['role'],
                phone=serializer.validated_data.get('phone'),
            )
            tokens = AuthService.generate_tokens(user)

            return created_response(
                data={
                    'user': {
                        'id': str(user.id),
                        'email': user.email,
                        'role': user.role,
                        'is_active': user.is_active,
                    },
                    'tokens': tokens,
                },
                message='Registration successful',
            )
        except ValueError as e:
            return bad_request_response(message=str(e))


class LoginView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        tags=['Authentication'],
        summary='Login with email and password',
    )
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            user, tokens = AuthService.login(
                email=serializer.validated_data['email'],
                password=serializer.validated_data['password'],
            )

            return success_response(
                data={
                    'user': {
                        'id': str(user.id),
                        'email': user.email,
                        'role': user.role,
                        'is_active': user.is_active,
                    },
                    'tokens': tokens,
                },
                message='Login successful',
            )
        except ValueError as e:
            return unauthorized_response(message=str(e))


class RefreshTokenView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        tags=['Authentication'],
        summary='Refresh access token',
    )
    def post(self, request):
        serializer = RefreshTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            tokens = AuthService.refresh_token(
                serializer.validated_data['refresh']
            )
            return success_response(data=tokens, message='Token refreshed')
        except ValueError as e:
            return unauthorized_response(message=str(e))


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=['Authentication'],
        summary='Logout and blacklist refresh token',
    )
    def post(self, request):
        serializer = LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        AuthService.logout(serializer.validated_data['refresh'])
        return success_response(message='Logged out successfully')


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=['Authentication'],
        summary='Get current user profile',
    )
    def get(self, request):
        user = request.user
        return success_response(
            data={
                'id': str(user.id),
                'email': user.email,
                'phone': user.phone,
                'role': user.role,
                'is_active': user.is_active,
                'is_email_verified': user.is_email_verified,
                'is_phone_verified': user.is_phone_verified,
                'last_login': str(user.last_login) if user.last_login else None,
                'created_at': str(user.created_at),
            }
        )
