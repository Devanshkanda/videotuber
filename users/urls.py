from django.urls import path
from .views import *

urlpatterns = [
    path('register/', get_details, name="get_details")
]
