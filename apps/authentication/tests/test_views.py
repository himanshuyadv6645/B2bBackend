from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status

User = get_user_model()


class RegisterAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = '/api/v1/auth/register/'
        # Disable throttling for tests
        from apps.authentication.views.register import RegisterView
        self._original_throttle = RegisterView.throttle_classes
        RegisterView.throttle_classes = []

    def tearDown(self):
        from apps.authentication.views.register import RegisterView
        RegisterView.throttle_classes = self._original_throttle

    def test_register_buyer(self):
        data = {
            'email': 'buyer@example.com',
            'password': 'testpass123',
            'confirm_password': 'testpass123',
            'role': 'buyer',
        }
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data['success'])

    def test_register_seller(self):
        data = {
            'email': 'seller@example.com',
            'password': 'testpass123',
            'confirm_password': 'testpass123',
            'role': 'seller',
        }
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_duplicate_email(self):
        User.objects.create_user(email='exists@example.com', password='testpass123')
        data = {
            'email': 'exists@example.com',
            'password': 'testpass123',
            'confirm_password': 'testpass123',
            'role': 'buyer',
        }
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_password_mismatch(self):
        data = {
            'email': 'buyer@example.com',
            'password': 'testpass123',
            'confirm_password': 'differentpass',
            'role': 'buyer',
        }
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class LoginAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.login_url = '/api/v1/auth/login/'
        from apps.authentication.views.register import LoginView
        self._original_throttle = LoginView.throttle_classes
        LoginView.throttle_classes = []

    def tearDown(self):
        from apps.authentication.views.register import LoginView
        LoginView.throttle_classes = self._original_throttle

    def test_login_success(self):
        User.objects.create_user(email='test@example.com', password='testpass123', role='buyer')
        data = {
            'email': 'test@example.com',
            'password': 'testpass123',
        }
        response = self.client.post(self.login_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('tokens', response.data['data'])

    def test_login_wrong_password(self):
        User.objects.create_user(email='test@example.com', password='testpass123')
        data = {
            'email': 'test@example.com',
            'password': 'wrongpass',
        }
        response = self.client.post(self.login_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_login_nonexistent_user(self):
        data = {
            'email': 'nonexistent@example.com',
            'password': 'testpass123',
        }
        response = self.client.post(self.login_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
