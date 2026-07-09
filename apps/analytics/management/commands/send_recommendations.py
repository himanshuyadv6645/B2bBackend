"""Send personalised product recommendations based on weighted behaviour.

Simple, no-Celery flow: run on a cron (e.g. once or twice a day).

For every user with recent activity it aggregates their events grouped by
product, weights each event by priority (see analytics/priorities.py), and picks
the highest-scoring product. If that score clears a threshold and the product is
still active and hasn't been recommended recently, it sends a recommendation
notification (in-app + push, with the product image and a "View product"
button).

    python manage.py send_recommendations --days 30 --dry-run

Weighting recap: payment/checkout/cart and wishlist score high, product views
medium, category/subcategory clicks low. So a product the user added to cart or
wishlisted easily outranks one they only glanced at from a category page.
"""
from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta

from apps.analytics.services import AnalyticsService
from apps.analytics.priorities import (
    RECOMMENDATION_MIN_SCORE,
    RECOMMENDATION_COOLDOWN_DAYS,
)
from apps.notifications.models import Notification
from apps.notifications.services import NotificationService


class Command(BaseCommand):
    help = 'Send personalised recommendations from weighted behaviour scores'

    def add_arguments(self, parser):
        parser.add_argument('--days', type=int, default=30,
                            help='How far back to score behaviour')
        parser.add_argument('--min-score', type=int, default=RECOMMENDATION_MIN_SCORE,
                            help='Minimum weighted score to send a recommendation')
        parser.add_argument('--dry-run', action='store_true',
                            help='Report what would be sent without sending')

    def handle(self, *args, **options):
        # Imported lazily so the analytics app has no hard dependency on products.
        from apps.products.models import Product
        from apps.authentication.models import User

        days = options['days']
        min_score = options['min_score']
        dry_run = options['dry_run']

        user_ids = AnalyticsService.get_users_with_recent_activity(days=days)
        cooldown_start = timezone.now() - timedelta(days=RECOMMENDATION_COOLDOWN_DAYS)

        sent = 0
        for uid in user_ids:
            scores = AnalyticsService.get_user_recommendation_scores(uid, days=days)
            if not scores:
                continue

            # Walk products best-first; take the first one that qualifies.
            for row in scores:
                if row['score'] < min_score:
                    break  # rest are lower, nothing else qualifies

                product = Product.objects.filter(id=row['entity_id'], is_active=True).first()
                if not product:
                    continue  # deleted / inactive -> try next best

                # De-dup: skip if already recommended within the cooldown window.
                already = Notification.objects.filter(
                    user_id=uid,
                    reference_type='recommendation',
                    reference_id=product.id,
                    created_at__gte=cooldown_start,
                ).exists()
                if already:
                    continue

                if dry_run:
                    self.stdout.write(
                        f'[dry-run] user {uid} -> "{product.name}" (score={row["score"]})'
                    )
                    sent += 1
                    break

                user = User.objects.filter(id=uid).first()
                if not user:
                    break

                image = product.images.filter(is_primary=True).first() \
                    or product.images.first()
                NotificationService.create_notification(
                    user=user,
                    notification_type='promotion',
                    title='Recommended for you',
                    message=f'Based on your interest: {product.name}',
                    reference_type='recommendation',
                    reference_id=product.id,
                    action_url=f'/products/{product.slug}',
                    push_data={
                        'image_url': image.image_url if image else None,
                        'button_text': 'View product',
                    },
                )
                self.stdout.write(self.style.SUCCESS(
                    f'[*] Recommended "{product.name}" to {user.full_name} '
                    f'({user.email}) score={row["score"]}'
                ))
                sent += 1
                break  # one recommendation per user per run

        self.stdout.write(self.style.SUCCESS(
            f'Recommendations: {len(user_ids)} active user(s), {sent} sent'
        ))
