from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CustomUserCreate, UserEventsAPIView


urlpatterns = [
    path('register/', CustomUserCreate.as_view(), name='user-register'),
    path('events/', UserEventsAPIView.as_view(), name='user-events'),
    path('token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]
