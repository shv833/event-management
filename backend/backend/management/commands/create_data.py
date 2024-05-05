from django.core.management.base import BaseCommand
from django.utils import timezone
from users.models import CustomUser
from events.models import Event
import random

class Command(BaseCommand):
    help = 'Creates sample events and users'

    def handle(self, *args, **kwargs):
        self.create_users()
        self.create_events()

    def create_users(self):
        for i in range(5):
            CustomUser.objects.create_user(
                email=f'user{i + 1}@example.com',
                password='password',
                first_name=f'First{i + 1}',
                last_name=f'Last{i + 1}',
                is_active=True,
                is_staff=False,
            )

    def create_events(self):
        users = CustomUser.objects.all()

        for i in range(10):
            organizer = random.choice(users)

            event = Event.objects.create(
                title=f'Event {i + 1}',
                description=f'Description for Event {i + 1}',
                date=timezone.now(),
                location=f'Location {i + 1}',
                organizer=organizer,
            )

            num_attendees = random.randint(0, len(users))
            attendees = random.sample(list(users), num_attendees)
            event.attendees.add(*attendees)
