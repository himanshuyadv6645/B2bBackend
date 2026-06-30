from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = 'Create a super admin user'

    def add_arguments(self, parser):
        parser.add_argument('--email', type=str, required=True)
        parser.add_argument('--password', type=str, required=True)

    def handle(self, *args, **options):
        email = options['email']
        password = options['password']

        if User.objects.filter(email=email).exists():
            self.stdout.write(self.style.ERROR(f'User {email} already exists'))
            return

        user = User.objects.create_superuser(
            email=email,
            password=password,
            role='admin',
        )
        self.stdout.write(self.style.SUCCESS(f'Superuser {email} created successfully'))
