from rest_framework import generics, status
from rest_framework.response import Response
from .models import Event
from .serializers import EventSerializer
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.exceptions import ObjectDoesNotExist
from .permissions import IsAdminOrEventOwner

class EventListCreateAPIView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]


class EventRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]


class EventAttendAPIView(generics.UpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        event = self.get_object()
        user = self.request.user

        try:
            if event.attendees.filter(pk=user.pk).exists():
                return Response({'message': 'User is already an attendee'}, status=status.HTTP_400_BAD_REQUEST)
            
            event.attendees.add(user)

            subject = 'Welcome for Event: {}'.format(event.title)
            message = render_to_string('event_attendee_notification_email.html', {'user': user, 'event': event})
            recipient_list = [user.email]
            send_mail(subject, message, None, recipient_list)

            return Response({'message': 'User added to event attendees successfully'}, status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            return Response({'message': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)


class EventUnattendAPIView(generics.UpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        event = self.get_object()
        user = self.request.user

        try:
            if not event.attendees.filter(pk=user.pk).exists():
                return Response({'message': 'User is not an attendee of this event'}, status=status.HTTP_400_BAD_REQUEST)
            
            event.attendees.remove(user)

            subject = 'Unregister from Event: {}'.format(event.title)
            message = render_to_string('event_unattendee_notification_email.html', {'user': user, 'event': event})
            recipient_list = [user.email]
            send_mail(subject, message, None, recipient_list)

            return Response({'message': 'User unregistered from event successfully'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'message': 'An error occurred while unregistering user from event'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)