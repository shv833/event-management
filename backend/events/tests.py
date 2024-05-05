from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Event
from users.models import CustomUser


class EventModelTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(email='test@example.com',
                                                   password='password123')
        self.event = Event.objects.create(title='Test Event',
                                          description='Test description',
                                          date='2024-05-01',
                                          location='Test location',
                                          organizer=self.user)

    def test_event_representation(self):
        self.assertEqual(str(self.event), self.event.title)


class EventAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(email='test@example.com',
                                                   password='password123')
        self.client.force_authenticate(user=self.user)
        self.event = Event.objects.create(title='Test Event',
                                          description='Test description',
                                          date='2024-05-01',
                                          location='Test location',
                                          organizer=self.user)

    def test_event_list(self):
        url = reverse('event-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_event_create(self):
        url = reverse('event-list-create')
        data = {
            'title': 'New Event',
            'description': 'New description',
            'date': '2024-06-01',
            'location': 'New location',
            'organizer': self.user.pk,
            }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_event_retrieve(self):
        url = reverse('event-retrieve', kwargs={'pk': self.event.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_event_delete(self):
        url = reverse('event-destroy', kwargs={'pk': self.event.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_event_attend(self):
        url = reverse('event-attend', kwargs={'pk': self.event.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_event_unattend(self):
        self.event.attendees.add(self.user)
        url = reverse('event-unattend', kwargs={'pk': self.event.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
