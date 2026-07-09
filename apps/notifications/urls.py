from django.urls import path
from apps.notifications.views.notification import (
    NotificationListView,
    NotificationDetailView,
    MarkNotificationReadView,
    MarkAllNotificationsReadView,
    UnreadNotificationCountView,
)
from apps.notifications.views.device import (
    RegisterDeviceView,
    UnregisterDeviceView,
)
from apps.notifications.views.admin import AdminBroadcastView

app_name = 'notifications'

urlpatterns = [
    path('', NotificationListView.as_view(), name='notification-list'),
    path('unread-count/', UnreadNotificationCountView.as_view(), name='unread-count'),
    path('devices/register/', RegisterDeviceView.as_view(), name='device-register'),
    path('devices/unregister/', UnregisterDeviceView.as_view(), name='device-unregister'),
    path('<uuid:pk>/', NotificationDetailView.as_view(), name='notification-detail'),
    path('<uuid:pk>/read/', MarkNotificationReadView.as_view(), name='mark-read'),
    path('read-all/', MarkAllNotificationsReadView.as_view(), name='mark-all-read'),
    path('admin/broadcast/', AdminBroadcastView.as_view(), name='admin-broadcast'),
]
