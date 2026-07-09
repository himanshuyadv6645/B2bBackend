from rest_framework import generics, serializers, status
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from common.permissions import IsAdminUser
from common.response import success_response
from apps.notifications.services import PushService


class BroadcastNotificationSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    body = serializers.CharField(max_length=1000)
    action_url = serializers.CharField(max_length=500, required=False, allow_blank=True)
    image_url = serializers.URLField(max_length=500, required=False, allow_blank=True)
    button_text = serializers.CharField(max_length=100, required=False, allow_blank=True)


class AdminBroadcastView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = BroadcastNotificationSerializer

    @extend_schema(
        tags=['Notifications - Admin'],
        summary='Send a push notification to all active users (Global Broadcast)',
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        title = serializer.validated_data['title']
        body = serializer.validated_data['body']
        action_url = serializer.validated_data.get('action_url')
        image_url = serializer.validated_data.get('image_url')
        button_text = serializer.validated_data.get('button_text')
        
        data_payload = {}
        if action_url:
            data_payload['action_url'] = action_url
        if image_url:
            data_payload['image_url'] = image_url
        if button_text:
            data_payload['button_text'] = button_text
        
        success_count = PushService.broadcast(
            title=title,
            body=body,
            data=data_payload
        )
        return success_response(
            message=f'Broadcast sent to {success_count} devices successfully.'
        )
