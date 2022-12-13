from django.urls import path
from accounts.api.views import RegistrationAV, EmailVerificationAV
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', RegistrationAV.as_view()),
    path('emailVerify/', EmailVerificationAV.as_view()),
    path('login/', obtain_auth_token),
]