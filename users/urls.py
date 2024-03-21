from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r"user-details", viewset=userViewSet, basename="get details")

urlpatterns = [
    path('', include(router.urls)),
]
