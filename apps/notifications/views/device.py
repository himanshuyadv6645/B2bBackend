from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

from apps.notifications.serializers.device import (
    DeviceRegisterSerializer,
    DeviceUnregisterSerializer,
)
from apps.notifications.services import PushService
from common.response import success_response


class RegisterDeviceView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(tags=['Notifications'], summary='Register a device for push',
                   request=DeviceRegisterSerializer)
    def post(self, request):
        serializer = DeviceRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        PushService.register_device(
            user=request.user,
            token=serializer.validated_data['token'],
            platform=serializer.validated_data.get('platform', 'web'),
            user_agent=request.META.get('HTTP_USER_AGENT', ''),
        )
        return success_response(message='Device registered')


class UnregisterDeviceView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(tags=['Notifications'], summary='Unregister a device from push',
                   request=DeviceUnregisterSerializer)
    def post(self, request):
        serializer = DeviceUnregisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        PushService.unregister_device(serializer.validated_data['token'])
        return success_response(message='Device unregistered')
