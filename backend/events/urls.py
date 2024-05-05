from django.urls import path
from .views import EventListCreateAPIView, EventRetrieveUpdateDestroyAPIView, EventAttendAPIView, EventUnattendAPIView


urlpatterns = [
    path('', EventListCreateAPIView.as_view(), name='event-list-create'),
    path('<int:pk>/', EventRetrieveUpdateDestroyAPIView.as_view(), name='event-retrieve-update-destroy'),
    path('<int:pk>/attend/', EventAttendAPIView.as_view(), name='event-attend'),
    path('<int:pk>/unattend/', EventUnattendAPIView.as_view(), name='event-unattend'),
]
