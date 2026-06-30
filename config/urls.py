from django.contrib import admin
from django.db import connection
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)


class HealthCheckView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        db_ok = True
        try:
            connection.ensure_connection()
        except Exception:
            db_ok = False

        data = {
            'status': 'healthy' if db_ok else 'degraded',
            'database': 'connected' if db_ok else 'disconnected',
        }

        if request.user and request.user.is_authenticated:
            data['authenticated'] = True
            data['user'] = request.user.email
        else:
            data['authenticated'] = False

        return Response(data, status=200 if db_ok else 503)


urlpatterns = [
    path('admin/', admin.site.urls),

    # Health
    path('api/v1/health/', HealthCheckView.as_view(), name='health-check'),

    # API Schema
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # API Endpoints
    path('api/v1/auth/', include('apps.authentication.urls')),
    path('api/v1/users/', include('apps.users.urls')),
    path('api/v1/buyers/', include('apps.buyers.urls')),
    path('api/v1/sellers/', include('apps.sellers.urls')),
    path('api/v1/categories/', include('apps.categories.urls')),
    path('api/v1/brands/', include('apps.brands.urls')),
    path('api/v1/products/', include('apps.products.urls')),
    path('api/v1/variants/', include('apps.product_variants.urls')),
    path('api/v1/pricing/', include('apps.pricing.urls')),
    path('api/v1/inventory/', include('apps.inventory.urls')),
    path('api/v1/wishlist/', include('apps.wishlist.urls')),
    path('api/v1/cart/', include('apps.cart.urls')),
    path('api/v1/orders/', include('apps.orders.urls')),
    path('api/v1/reviews/', include('apps.reviews.urls')),
    path('api/v1/notifications/', include('apps.notifications.urls')),
    path('api/v1/dashboard/', include('apps.dashboard.urls')),
    path('api/v1/analytics/', include('apps.analytics.urls')),
    path('api/v1/payments/', include('apps.payments.urls')),

    # SEO (API + sitemap + robots)
    path('api/v1/seo/', include('apps.seo.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
