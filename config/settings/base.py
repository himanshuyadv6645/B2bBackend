import os
from pathlib import Path
from datetime import timedelta
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = config('DJANGO_SECRET_KEY', default='django-insecure-change-me-in-production')

DEBUG = config('DJANGO_DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ['*']

SITE_URL = config('SITE_URL', default='http://localhost:5173')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt',
    'django_filters',
    'drf_spectacular',
    'cloudinary',

    # Local apps
    'apps.authentication',
    'apps.users',
    'apps.buyers',
    'apps.sellers',
    'apps.categories',
    'apps.brands',
    'apps.products',
    'apps.product_variants',
    'apps.pricing',
    'apps.inventory',
    'apps.wishlist',
    'apps.cart',
    'apps.orders',
    'apps.reviews',
    'apps.notifications',
    'apps.dashboard',
    'apps.analytics',
    'apps.payments',
    'apps.banners',
    'apps.seo',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # WhiteNoise serves static files (admin + DRF browsable API CSS) in production
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

AUTH_USER_MODEL = 'authentication.User'

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Django 6 storages API (replaces the removed DEFAULT_FILE_STORAGE / STATICFILES_STORAGE).
# WhiteNoise compresses static files so the admin & DRF browsable API are styled in prod.
STORAGES = {
    'default': {
        'BACKEND': 'django.core.files.storage.FileSystemStorage',
    },
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedStaticFilesStorage',
    },
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_PAGINATION_CLASS': 'common.pagination.StandardResultsPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'EXCEPTION_HANDLER': 'common.exceptions.custom_exception_handler',
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(
        minutes=config('JWT_ACCESS_TOKEN_LIFETIME_MINUTES', default=30, cast=int)
    ),
    'REFRESH_TOKEN_LIFETIME': timedelta(
        days=config('JWT_REFRESH_TOKEN_LIFETIME_DAYS', default=7, cast=int)
    ),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'B2B Wholesale Electronics Marketplace',
    'DESCRIPTION': 'B2B Wholesale Electronics Marketplace API',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'COMPONENT_SPLIT_REQUEST': True,
    'TAGS': [
        {'name': 'Authentication', 'description': 'Registration, Login, Token'},
        {'name': 'Users', 'description': 'User profile management'},
        {'name': 'Buyers', 'description': 'Buyer profiles and addresses'},
        {'name': 'Sellers', 'description': 'Seller profiles and warehouses'},
        {'name': 'Categories', 'description': 'Product categories'},
        {'name': 'Brands', 'description': 'Product brands'},
        {'name': 'Products', 'description': 'Product management'},
        {'name': 'Product Variants', 'description': 'Product variant management'},
        {'name': 'Pricing', 'description': 'Seller pricing management'},
        {'name': 'Inventory', 'description': 'Stock management'},
        {'name': 'Wishlist', 'description': 'Buyer wishlist'},
        {'name': 'Cart', 'description': 'Shopping cart'},
        {'name': 'Orders', 'description': 'Order management'},
        {'name': 'Reviews', 'description': 'Product and seller reviews'},
        {'name': 'Notifications', 'description': 'In-app notifications'},
        {'name': 'Dashboard', 'description': 'Dashboard data'},
        {'name': 'Analytics', 'description': 'Analytics events'},
    ],
}

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config('CLOUDINARY_CLOUD_NAME', default=''),
    'API_KEY': config('CLOUDINARY_API_KEY', default=''),
    'API_SECRET': config('CLOUDINARY_API_SECRET', default=''),
}

CORS_ALLOW_ALL_ORIGINS = DEBUG

# Firebase Cloud Messaging (push notifications).
# Provide the service-account credentials via EITHER:
#   FIREBASE_CREDENTIALS_JSON  - the raw service-account JSON as a string (best
#                                for Render/hosted env vars), OR
#   FIREBASE_CREDENTIALS_FILE  - a path to the service-account .json file.
# If neither is set, push is silently disabled (in-app notifications still work).
FIREBASE_CREDENTIALS_JSON = config('FIREBASE_CREDENTIALS_JSON', default='')
FIREBASE_CREDENTIALS_FILE = config('FIREBASE_CREDENTIALS_FILE', default='')
