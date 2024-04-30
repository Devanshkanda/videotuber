from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r"videos", viewset=VideosViewSet, basename="show all videos")

urlpatterns = [
    path('', include(router.urls))
]
