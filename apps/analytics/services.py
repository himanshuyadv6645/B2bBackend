from django.db.models import Count
from django.utils import timezone
from datetime import timedelta
from apps.analytics.models import AnalyticsEvent


class AnalyticsService:
    @staticmethod
    def track_event(user, event_type, entity_type=None, entity_id=None, metadata=None, request=None):
        ip_address = None
        user_agent = None
        session_id = None

        if request:
            ip_address = AnalyticsService.get_client_ip(request)
            user_agent = request.META.get('HTTP_USER_AGENT', '')[:500]
            session_id = request.META.get('HTTP_SESSION_KEY', None)

        event = AnalyticsEvent.objects.create(
            user=user,
            event_type=event_type,
            entity_type=entity_type,
            entity_id=entity_id,
            metadata=metadata,
            ip_address=ip_address,
            user_agent=user_agent,
            session_id=session_id,
        )
        return event

    @staticmethod
    def get_client_ip(request):
        x_forwarded = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded:
            return x_forwarded.split(',')[0].strip()
        return request.META.get('REMOTE_ADDR')

    @staticmethod
    def get_event_stats(event_type=None, days=30):
        start_date = timezone.now() - timedelta(days=days)
        queryset = AnalyticsEvent.objects.filter(created_at__gte=start_date)

        if event_type:
            queryset = queryset.filter(event_type=event_type)

        return queryset.values('event_type').annotate(count=Count('id')).order_by('-count')

    @staticmethod
    def get_popular_entities(entity_type, limit=10):
        return AnalyticsEvent.objects.filter(
            entity_type=entity_type,
            event_type='product_view',
        ).values('entity_id').annotate(
            count=Count('id')
        ).order_by('-count')[:limit]

    @staticmethod
    def get_daily_events(days=30):
        start_date = timezone.now() - timedelta(days=days)
        return AnalyticsEvent.objects.filter(
            created_at__gte=start_date
        ).extra(
            select={'day': "date(created_at)"}
        ).values('day').annotate(count=Count('id')).order_by('day')
