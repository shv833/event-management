from django.db import models
from users.models import CustomUser
from ckeditor.fields import RichTextField


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    organizer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    attendees = models.ManyToManyField(CustomUser, related_name='attended_events', blank=True)

    def __str__(self):
        return self.title
