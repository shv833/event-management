from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import CustomUser


class CustomUserModelTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(email='test@example.com',
                                                   password='password123')

    def test_user_representation(self):
        self.assertEqual(str(self.user), self.user.email)


class CustomUserCreateAPIViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(email='new@example.com',
                                                   password='newpassword123')

    def test_create_user(self):
        url = reverse('user-register')
        data = {'email': 'neew@example.com', 'password': 'newpassword123'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_tokens_user(self):
        url = reverse('token-obtain-pair')
        data = {'email': 'new@example.com', 'password': 'newpassword123'}
        response = self.client.post(url, data)
        self.assertTrue('access' in response.data)
        self.assertTrue('refresh' in response.data)

    def test_invalid_data(self):
        url = reverse('user-register')
        data = {'email': 'newuser', 'password': 'newpassword123'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UserEventsAPIViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(email='test@example.com',
                                                   password='password123')
        self.client.force_authenticate(user=self.user)

    def test_user_events_list(self):
        url = reverse('user-events')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_access(self):
        self.client.logout()
        url = reverse('user-events')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
