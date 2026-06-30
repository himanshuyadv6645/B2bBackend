from .base import *
import os
import urllib.parse
import socket

DEBUG = False

ALLOWED_HOSTS = config('DJANGO_ALLOWED_HOSTS', default='*').split(',')

def get_ipv4_addr(host):
    try:
        ip = socket.gethostbyname(host)
        return ip
    except socket.gaierror:
        return host

DATABASE_URL = config('DATABASE_URL', default='')
if DATABASE_URL:
    url = urllib.parse.urlparse(DATABASE_URL)
    host = url.hostname or ''
    ipv4 = get_ipv4_addr(host)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': url.path[1:].split('?')[0],
            'USER': url.username or '',
            'PASSWORD': url.password or '',
            'HOST': host,
            'PORT': url.port or 5432,
            'CONN_MAX_AGE': 600,
            'OPTIONS': {
                'sslmode': 'require',
                'hostaddr': ipv4,
            },
        }
    }
else:
    db_host = config('DATABASE_HOST', default='')
    ipv4 = get_ipv4_addr(db_host)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': config('DATABASE_NAME', default='postgres'),
            'USER': config('DATABASE_USER', default='postgres'),
            'PASSWORD': config('DATABASE_PASSWORD', default=''),
            'HOST': db_host,
            'PORT': config('DATABASE_PORT', default='5432'),
            'CONN_MAX_AGE': 600,
            'OPTIONS': {
                'sslmode': 'require',
                'hostaddr': ipv4,
            },
        }
    }

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config('CLOUDINARY_CLOUD_NAME', default=''),
    'API_KEY': config('CLOUDINARY_API_KEY', default=''),
    'API_SECRET': config('CLOUDINARY_API_SECRET', default=''),
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

CORS_ALLOW_ALL_ORIGINS = False
