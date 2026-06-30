from django.urls import path
from apps.categories.views.category import (
    CategoryListView,
    CategoryDetailView,
    CategoryTreeView,
    CategoryFeaturedView,
    CategorySearchView,
    CategoryAdminListView,
    AdminCategoryCreateView,
    AdminCategoryUpdateView,
    AdminCategoryDeleteView,
    AdminCategoryBulkStatusView,
)

app_name = 'categories'

urlpatterns = [
    # Public endpoints
    path('', CategoryListView.as_view(), name='category-list'),
    path('tree/', CategoryTreeView.as_view(), name='category-tree'),
    path('featured/', CategoryFeaturedView.as_view(), name='category-featured'),
    path('search/', CategorySearchView.as_view(), name='category-search'),
    path('<slug:slug>/', CategoryDetailView.as_view(), name='category-detail'),

    # Admin endpoints
    path('admin/list/', CategoryAdminListView.as_view(), name='admin-category-list'),
    path('admin/create/', AdminCategoryCreateView.as_view(), name='admin-category-create'),
    path('admin/<uuid:pk>/', AdminCategoryUpdateView.as_view(), name='admin-category-update'),
    path('admin/<uuid:pk>/delete/', AdminCategoryDeleteView.as_view(), name='admin-category-delete'),
    path('admin/bulk-status/', AdminCategoryBulkStatusView.as_view(), name='admin-category-bulk-status'),
]
