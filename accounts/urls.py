from django.urls import path
from . import  views
urlpatterns = [
    path('register/',views.RegisterAPIView.as_view()),
    path('profile/',views.ProfileAPIView.as_view()),
]
