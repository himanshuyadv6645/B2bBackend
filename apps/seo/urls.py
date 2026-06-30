from django.urls import path
from . import views

urlpatterns = [
    path('resolve/<path:path>/', views.SEOResolveView.as_view(), name='seo-resolve'),
    path('generate/', views.SEOGenerateView.as_view(), name='seo-generate'),
    path('sitemap.xml', views.SEOSitemapView.as_view(), name='seo-sitemap'),
    path('robots.txt', views.SEORobotsView.as_view(), name='seo-robots'),
]
