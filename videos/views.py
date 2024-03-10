from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
# Create your views here.


class showAllVideos(ModelViewSet):
    queryset = videos.objects.all()
    serializer_class = []
    