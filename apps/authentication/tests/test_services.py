from django.test import TestCase
from django.contrib.auth import get_user_model
from apps.authentication.services import AuthService

User = get_user_model()


class AuthServiceTest(TestCase):
    def test_register_user(self):
        user = AuthService.register(
            email='service@example.com',
            password='testpass123',
            role='buyer',
        )
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, 'service@example.com')

    def test_register_duplicate_email(self):
        AuthService.register(email='dup@example.com', password='testpass123')
        with self.assertRaises(ValueError):
            AuthService.register(email='dup@example.com', password='testpass123')

    def test_login_success(self):
        AuthService.register(email='login@example.com', password='testpass123')
        user, tokens = AuthService.login('login@example.com', 'testpass123')
        self.assertIsInstance(user, User)
        self.assertIn('access', tokens)
        self.assertIn('refresh', tokens)

    def test_login_wrong_password(self):
        AuthService.register(email='login2@example.com', password='testpass123')
        with self.assertRaises(ValueError):
            AuthService.login('login2@example.com', 'wrongpass')

    def test_generate_tokens(self):
        user = User.objects.create_user(email='token@example.com', password='testpass123')
        tokens = AuthService.generate_tokens(user)
        self.assertIn('access', tokens)
        self.assertIn('refresh', tokens)
