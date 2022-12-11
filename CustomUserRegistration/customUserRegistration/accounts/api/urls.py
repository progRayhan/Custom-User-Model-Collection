from django.urls import path
from accounts.api.views import RegistrationAV, EmailVerificationAV

urlpatterns = [
    path('register/', RegistrationAV.as_view()),
    path('emailVerify/', EmailVerificationAV.as_view()),
]