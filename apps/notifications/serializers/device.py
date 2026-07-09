from rest_framework import serializers


class DeviceRegisterSerializer(serializers.Serializer):
    token = serializers.CharField()
    platform = serializers.ChoiceField(
        choices=['web', 'android', 'ios'], required=False, default='web',
    )


class DeviceUnregisterSerializer(serializers.Serializer):
    token = serializers.CharField()
