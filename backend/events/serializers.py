from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    organizer_email = serializers.EmailField(source='organizer.email', read_only=True)
    attendees = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date', 'location', 'organizer', 'organizer_email', 'attendees']

    def get_attendees(self, obj):
        attendees_emails = obj.attendees.values_list('email', flat=True)
        # attendees_ids = obj.attendees.values_list('id', flat=True)
        # attendees_dict = {id: email for id, email in zip(attendees_ids, attendees_emails)}
        # return attendees_dict
        return attendees_emails
