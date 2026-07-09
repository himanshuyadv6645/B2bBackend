from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from drf_spectacular.utils import extend_schema

from apps.analytics.serializers.analytics import TrackEventSerializer
from apps.analytics.services import AnalyticsService
from common.response import success_response


class TrackEventView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(tags=['Analytics'], summary='Track analytics event')
    def post(self, request):
        serializer = TrackEventSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user if request.user.is_authenticated else None

        event = AnalyticsService.track_event(
            user=user,
            event_type=serializer.validated_data['event_type'],
            entity_type=serializer.validated_data.get('entity_type'),
            entity_id=serializer.validated_data.get('entity_id'),
            metadata=serializer.validated_data.get('metadata', {}),
            request=request,
        )
        return success_response(message='Event tracked')


class EventStatsView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(tags=['Analytics'], summary='Get event statistics')
    def get(self, request):
        event_type = request.query_params.get('event_type')
        days = int(request.query_params.get('days', 30))
        stats = AnalyticsService.get_event_stats(event_type, days)
        return success_response(data=list(stats))


class PopularEntitiesView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(tags=['Analytics'], summary='Get popular entities')
    def get(self, request):
        entity_type = request.query_params.get('entity_type', 'product')
        limit = int(request.query_params.get('limit', 10))
        popular = AnalyticsService.get_popular_entities(entity_type, limit)
        return success_response(data=list(popular))


class MyViewedProductsView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(tags=['Analytics'], summary='Get my most-viewed products')
    def get(self, request):
        limit = int(request.query_params.get('limit', 10))
        days = int(request.query_params.get('days', 90))
        data = AnalyticsService.get_user_most_viewed_products(
            request.user, limit=limit, days=days,
        )
        return success_response(data=list(data))
