from rest_framework import serializers
from apps.analytics.models import AnalyticsEvent


class AnalyticsEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnalyticsEvent
        fields = [
            'id', 'event_type', 'entity_type', 'entity_id',
            'metadata', 'created_at',
        ]


class TrackEventSerializer(serializers.Serializer):
    event_type = serializers.CharField(max_length=100)
    entity_type = serializers.CharField(max_length=50, required=False, allow_blank=True)
    entity_id = serializers.UUIDField(required=False, allow_null=True)
    metadata = serializers.DictField(required=False, allow_empty=True)
