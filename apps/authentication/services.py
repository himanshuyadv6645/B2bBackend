import random
import string
from datetime import timedelta
from django.utils import timezone
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
class AuthService:
    @staticmethod
    def register(email, password, role='buyer', phone=None):
        if User.objects.filter(email=email).exists():
            raise ValueError('Email already registered')

        if phone and User.objects.filter(phone=phone).exists():
            raise ValueError('Phone number already registered')

        user = User.objects.create_user(
            email=email,
            password=password,
            role=role,
            phone=phone,
        )
        return user

    @staticmethod
    def login(email, password):
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise ValueError('Invalid email or password')

        if not user.check_password(password):
            raise ValueError('Invalid email or password')

        if not user.is_active:
            raise ValueError('Account is disabled')

        from django.contrib.auth.models import update_last_login
        update_last_login(None, user)

        tokens = AuthService.generate_tokens(user)
        return user, tokens

    @staticmethod
    def generate_tokens(user):
        refresh = RefreshToken.for_user(user)
        refresh['role'] = user.role
        refresh['email'] = user.email

        return {
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }

    @staticmethod
    def refresh_token(refresh_token):
        try:
            token = RefreshToken(refresh_token)
            return {
                'access': str(token.access_token),
                'refresh': str(token),
            }
        except Exception:
            raise ValueError('Invalid or expired refresh token')

    @staticmethod
    def generate_otp():
        return ''.join(random.choices(string.digits, k=6))

    @staticmethod
    def logout(refresh_token):
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return True
        except Exception:
            return False
