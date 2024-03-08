from django.urls import path
from .views import *
from rest_framework import routers


urlpatterns = [
    path('register/', get_details, name="get_details")
]
