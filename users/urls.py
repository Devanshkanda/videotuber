from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r"register", viewset=get_details.as_view(), basename="get details")

urlpatterns = [
    path('', include('router.urls'))
]
