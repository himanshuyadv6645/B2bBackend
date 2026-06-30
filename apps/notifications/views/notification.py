from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

from apps.notifications.models import Notification
from apps.notifications.serializers.notification import (
    NotificationSerializer,
    NotificationListSerializer,
)
from apps.notifications.services import NotificationService
from common.response import success_response
from common.pagination import StandardResultsPagination


class NotificationListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NotificationListSerializer
    pagination_class = StandardResultsPagination

    def get_queryset(self):
        unread_only = self.request.query_params.get('unread', '').lower() == 'true'
        return NotificationService.get_notifications(self.request.user, unread_only)

    @extend_schema(tags=['Notifications'], summary='List your notifications')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class NotificationDetailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NotificationSerializer

    def get_object(self):
        return Notification.objects.get(id=self.kwargs['pk'], user=self.request.user)

    @extend_schema(tags=['Notifications'], summary='Get notification details')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class MarkNotificationReadView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(tags=['Notifications'], summary='Mark notification as read')
    def post(self, request, pk):
        NotificationService.mark_as_read(pk, request.user)
        return success_response(message='Notification marked as read')


class MarkAllNotificationsReadView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(tags=['Notifications'], summary='Mark all notifications as read')
    def post(self, request):
        NotificationService.mark_all_as_read(request.user)
        return success_response(message='All notifications marked as read')


class UnreadNotificationCountView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(tags=['Notifications'], summary='Get unread notification count')
    def get(self, request):
        count = NotificationService.get_unread_count(request.user)
        return success_response(data={'count': count})
