from datetime import timedelta
from django.utils import timezone
from django.core.management.base import BaseCommand
from apps.authentication.models import User
from apps.notifications.services import NotificationService

class Command(BaseCommand):
    help = 'Sends a push notification to users who have been inactive for a certain number of minutes (for testing).'

    def add_arguments(self, parser):
        parser.add_argument(
            '--minutes',
            type=int,
            default=5,
            help='Number of minutes of inactivity before sending a notification',
        )

    def handle(self, *args, **options):
        minutes = options['minutes']
        threshold_date = timezone.now() - timedelta(minutes=minutes)
        
        # Find users whose last_login is before the threshold date and are active.
        # Note: Users who have never logged in might have last_login as None, we exclude them.
        inactive_users = User.objects.filter(
            last_login__lte=threshold_date,
            is_active=True
        )
        
        count = 0
        for user in inactive_users:
            NotificationService.create_notification(
                user=user,
                notification_type='system',
                title='We miss you!',
                message=f'Hi {user.full_name}, it has been a while since your last visit. Check out our latest products!',
                send_push=True
            )
            self.stdout.write(self.style.SUCCESS(f'[*] Sent notification to: {user.full_name} ({user.email})'))
            count += 1
            
        self.stdout.write(self.style.SUCCESS(f'\nTotal: Successfully sent notifications to {count} inactive users (inactive for {minutes}+ minutes).'))
