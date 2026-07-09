"""Detect abandoned checkouts/payments and send a one-time reminder.

Simple, no-Celery flow: run on a cron (e.g. every 10-15 minutes).
Finds users who reached checkout / initiated payment but never completed the
order, and sends a single in-app reminder per abandonment.

    python manage.py detect_abandoned_payments --minutes 15 --window-hours 72

When Celery/Redis lands, this moves to a scheduled task with escalating
reminders (10 min, 1 hour, 1 day) and multi-channel delivery.
"""
from django.core.management.base import BaseCommand

from apps.analytics.services import AnalyticsService
from apps.notifications.models import Notification
from apps.notifications.services import NotificationService


class Command(BaseCommand):
    help = 'Detect abandoned checkouts/payments and send reminder notifications'

    def add_arguments(self, parser):
        parser.add_argument('--minutes', type=int, default=15,
                            help='Grace period after checkout before reminding')
        parser.add_argument('--window-hours', type=int, default=72,
                            help='How far back to look for abandoned checkouts')
        parser.add_argument('--dry-run', action='store_true',
                            help='Report candidates without creating notifications')

    def handle(self, *args, **options):
        candidates = AnalyticsService.get_abandoned_payments(
            minutes=options['minutes'],
            window_hours=options['window_hours'],
        )

        sent = 0
        for row in candidates:
            uid = row['user_id']
            last_checkout = row['last_checkout']

            already = Notification.objects.filter(
                user_id=uid,
                reference_type='payment_abandoned',
                created_at__gte=last_checkout,
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
                title='Complete your payment',
                message='You were almost done. Finish your checkout to place your order.',
                reference_type='payment_abandoned',
                action_url='/buyer/cart',
            )
            self.stdout.write(self.style.SUCCESS(f'[*] Sent abandoned payment reminder to: {user.full_name} ({user.email})'))
            sent += 1

        self.stdout.write(self.style.SUCCESS(
            f'Abandoned payments: {len(candidates)} candidate(s), {sent} reminder(s) sent'
        ))

    @staticmethod
    def _user(uid):
        from apps.authentication.models import User
        return User.objects.get(id=uid)
