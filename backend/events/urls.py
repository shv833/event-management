from django.urls import path
from .views import (EventCreateAPIView, EventListAPIView, EventRetrieveAPIView,
                    EventAttendAPIView, EventUnattendAPIView, EventDestroyAPIView)


urlpatterns = [
    path('', EventListAPIView.as_view(), name='event-list'),
    path('create/', EventCreateAPIView.as_view(), name='event-list-create'),
    path('<int:pk>/', EventRetrieveAPIView.as_view(), name='event-retrieve'),
    path('<int:pk>/delete/', EventDestroyAPIView.as_view(), name='event-destroy'),
    path('<int:pk>/attend/', EventAttendAPIView.as_view(), name='event-attend'),
    path('<int:pk>/unattend/', EventUnattendAPIView.as_view(), name='event-unattend'),
]
