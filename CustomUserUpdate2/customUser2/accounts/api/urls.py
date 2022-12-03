from django.urls import path
from accounts.api.views import RegistrationAV

urlpatterns = [
    path('register/', RegistrationAV.as_view())
]