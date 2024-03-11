from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r"file", viewset=userViewSet, basename="get details")

urlpatterns = [
    path('', include(router.urls)),
]
