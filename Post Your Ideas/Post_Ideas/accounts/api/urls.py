from django.urls import path
from accounts.api.views import ProfileListAV, ProfileDetailsAV

urlpatterns = [
    path('profilelist/', ProfileListAV.as_view()),
    path('profiledetails/<str:pk>/', ProfileDetailsAV.as_view()),
]