"""Detect abandoned carts and send a one-time reminder notification.

Simple, no-Celery flow: run this on a cron (e.g. every 15-30 minutes).
It reads the raw AnalyticsEvent log, finds users who added to cart but never
initiated payment, and drops an in-app reminder — once per abandonment.

    python manage.py detect_abandoned_carts --minutes 30 --window-hours 72

Later, when Celery/Redis is added, the same detection can move to a task and
gain email/SMS/push fan-out. The detection logic stays in AnalyticsService.
"""
from django.core.management.base import BaseCommand

from apps.analytics.services import AnalyticsService
from apps.analytics.models import AnalyticsEvent
from apps.notifications.models import Notification
from apps.notifications.services import NotificationService


class Command(BaseCommand):
    help = 'Detect abandoned carts and send reminder notifications'

    def add_arguments(self, parser):
        parser.add_argument('--minutes', type=int, default=30,
                            help='Grace period after add_to_cart before reminding')
        parser.add_argument('--window-hours', type=int, default=72,
                            help='How far back to look for abandoned carts')
        parser.add_argument('--dry-run', action='store_true',
                            help='Report candidates without creating notifications')

    def handle(self, *args, **options):
        candidates = AnalyticsService.get_abandoned_carts(
            minutes=options['minutes'],
            window_hours=options['window_hours'],
        )

        sent = 0
        for row in candidates:
            uid = row['user_id']
            last_add = row['last_add']

            # De-dup: skip if we already reminded this user since their last add.
            already = Notification.objects.filter(
                user_id=uid,
                reference_type='cart_abandoned',
                created_at__gte=last_add,
            ).exists()
            if already:
                continue

            if options['dry_run']:
                self.stdout.write(f'[dry-run] would remind user {uid}')
                sent += 1
                continue

            user = self._user(uid)
            NotificationService.create_notification(
                user=user,
                notification_type='promotion',
                title='You left items in your cart',
                message='Your cart is waiting. Complete your order before items sell out.',
                reference_type='cart_abandoned',
                reference_id=row.get('entity_id'),
                action_url='/buyer/cart',
            )
            self.stdout.write(self.style.SUCCESS(f'[*] Sent abandoned cart reminder to: {user.full_name} ({user.email})'))
            sent += 1

        self.stdout.write(self.style.SUCCESS(
            f'Abandoned carts: {len(candidates)} candidate(s), {sent} reminder(s) sent'
        ))

    @staticmethod
    def _user(uid):
        # create_notification takes a user instance; fetch lazily.
        from apps.authentication.models import User
        return User.objects.get(id=uid)
