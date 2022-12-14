from django.urls import path
from accounts.api.views import ProfileListAV, ProfileDetailsAV
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('profilelist/', ProfileListAV.as_view()),
    path('profiledetails/<str:pk>/', ProfileDetailsAV.as_view()),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]