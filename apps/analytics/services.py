from django.db.models import Count, Sum, Case, When, Value, IntegerField
from django.utils import timezone
from datetime import timedelta
from apps.analytics.models import AnalyticsEvent
from apps.analytics.priorities import EVENT_WEIGHTS, DEFAULT_WEIGHT


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
    def get_user_most_viewed_products(user, limit=10, days=90):
        """Products a given user viewed the most, recent-window first.

        Drives per-user recommendations, "new product in a category you browse"
        alerts, and offer targeting. Returns [{entity_id, count}].
        """
        start_date = timezone.now() - timedelta(days=days)
        return AnalyticsEvent.objects.filter(
            user=user,
            event_type='product_view',
            entity_type='product',
            entity_id__isnull=False,
            created_at__gte=start_date,
        ).values('entity_id').annotate(
            count=Count('id')
        ).order_by('-count')[:limit]

    @staticmethod
    def _weight_case():
        """A Case() that maps event_type -> priority weight (see priorities.py)."""
        whens = [When(event_type=et, then=Value(w)) for et, w in EVENT_WEIGHTS.items()]
        return Case(*whens, default=Value(DEFAULT_WEIGHT), output_field=IntegerField())

    @staticmethod
    def get_user_recommendation_scores(user, limit=10, days=30):
        """Score a user's products by weighted interest, highest first.

        This is the core of recommendations: take the user's product events in
        the window, weight each event by its priority (cart/wishlist high,
        category click low), group by product, and sum. Returns
        [{entity_id, score, events}] ordered by score desc.
        """
        start_date = timezone.now() - timedelta(days=days)
        return list(
            AnalyticsEvent.objects.filter(
                user=user,
                entity_type='product',
                entity_id__isnull=False,
                created_at__gte=start_date,
                event_type__in=EVENT_WEIGHTS.keys(),
            )
            .values('entity_id')
            .annotate(score=Sum(AnalyticsService._weight_case()), events=Count('id'))
            .order_by('-score', '-events')[:limit]
        )

    @staticmethod
    def get_user_category_scores(user, limit=5, days=30):
        """Weighted category interest for a user (category/subcategory clicks).

        Categories are tracked by slug in metadata (no product UUID), so we
        group on metadata->>'slug'. Lower-priority signal, kept for
        "new in a category you browse" style nudges.
        """
        start_date = timezone.now() - timedelta(days=days)
        return list(
            AnalyticsEvent.objects.filter(
                user=user,
                entity_type='category',
                created_at__gte=start_date,
                event_type__in=('category_view', 'subcategory_view'),
            )
            .values('metadata__slug')
            .annotate(score=Sum(AnalyticsService._weight_case()), events=Count('id'))
            .order_by('-score', '-events')[:limit]
        )

    @staticmethod
    def get_users_with_recent_activity(days=30):
        """Distinct user ids that have any weighted product event in the window.

        Used by the recommendation cron to know whom to score, instead of
        scanning every user in the system.
        """
        start_date = timezone.now() - timedelta(days=days)
        return list(
            AnalyticsEvent.objects.filter(
                user__isnull=False,
                entity_type='product',
                entity_id__isnull=False,
                created_at__gte=start_date,
                event_type__in=EVENT_WEIGHTS.keys(),
            )
            # Clear the model's default -created_at ordering, otherwise it is
            # added to the SELECT and breaks DISTINCT (returns duplicate users).
            .order_by('user_id')
            .values_list('user_id', flat=True)
            .distinct()
        )

    @staticmethod
    def get_abandoned_carts(minutes=30, window_hours=72):
        """Users who added to cart but did not initiate payment afterwards.

        Simple, no-Celery detection: within the last `window_hours`, find
        add_to_cart events older than `minutes` (grace period) whose user has no
        payment_initiated event after them. Returns a de-duplicated list of
        {user_id, entity_id (last product), last_add}.

        Meant to be called from a management command run on a cron.
        """
        now = timezone.now()
        window_start = now - timedelta(hours=window_hours)
        cutoff = now - timedelta(minutes=minutes)

        adds = AnalyticsEvent.objects.filter(
            event_type='add_to_cart',
            user__isnull=False,
            created_at__gte=window_start,
            created_at__lte=cutoff,
        ).order_by('user', '-created_at')

        results = {}
        for ev in adds:
            uid = ev.user_id
            if uid in results:
                continue  # keep only the most recent add per user
            paid_after = AnalyticsEvent.objects.filter(
                user_id=uid,
                event_type__in=['payment_initiated', 'order_placed'],
                created_at__gte=ev.created_at,
            ).exists()
            if not paid_after:
                results[uid] = {
                    'user_id': uid,
                    'entity_id': ev.entity_id,
                    'last_add': ev.created_at,
                }
        return list(results.values())

    @staticmethod
    def get_abandoned_payments(minutes=15, window_hours=72):
        """Users who reached checkout/payment but did not complete it.

        Finds checkout_started (or payment_initiated) events with no subsequent
        order_placed, older than `minutes`. Returns de-duplicated
        {user_id, last_checkout}. For a cron-driven reminder job.
        """
        now = timezone.now()
        window_start = now - timedelta(hours=window_hours)
        cutoff = now - timedelta(minutes=minutes)

        checkouts = AnalyticsEvent.objects.filter(
            event_type__in=['checkout_started', 'payment_initiated'],
            user__isnull=False,
            created_at__gte=window_start,
            created_at__lte=cutoff,
        ).order_by('user', '-created_at')

        results = {}
        for ev in checkouts:
            uid = ev.user_id
            if uid in results:
                continue
            placed_after = AnalyticsEvent.objects.filter(
                user_id=uid,
                event_type='order_placed',
                created_at__gte=ev.created_at,
            ).exists()
            if not placed_after:
                results[uid] = {
                    'user_id': uid,
                    'last_checkout': ev.created_at,
                }
        return list(results.values())

    @staticmethod
    def get_daily_events(days=30):
        start_date = timezone.now() - timedelta(days=days)
        return AnalyticsEvent.objects.filter(
            created_at__gte=start_date
        ).extra(
            select={'day': "date(created_at)"}
        ).values('day').annotate(count=Count('id')).order_by('day')
