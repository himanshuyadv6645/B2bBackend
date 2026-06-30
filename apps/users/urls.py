from django.urls import path
from apps.users.views.user import (
    ProfileView,
    ChangePasswordView,
    AdminUserListView,
    AdminUserDetailView,
    AdminToggleUserStatusView,
)

app_name = 'users'

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('admin/users/', AdminUserListView.as_view(), name='admin-user-list'),
    path('admin/users/<uuid:pk>/', AdminUserDetailView.as_view(), name='admin-user-detail'),
    path('admin/users/<uuid:user_id>/toggle-status/', AdminToggleUserStatusView.as_view(), name='admin-toggle-status'),
]
