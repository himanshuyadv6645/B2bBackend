from django.contrib.auth import get_user_model
from django.test import TestCase


User = get_user_model()


class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(
            email='test@example.com',
            password='testpass123',
            role='buyer',
        )
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.role, 'buyer')
        self.assertTrue(user.check_password('testpass123'))
        self.assertTrue(user.is_active)

    def test_create_superuser(self):
        user = User.objects.create_superuser(
            email='admin@example.com',
            password='adminpass123',
        )
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        self.assertEqual(user.role, 'admin')

    def test_user_str(self):
        user = User.objects.create_user(
            email='test@example.com',
            password='testpass123',
        )
        self.assertEqual(str(user), 'test@example.com (buyer)')
