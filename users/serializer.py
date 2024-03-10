from rest_framework.serializers import ModelSerializer
from .models import *


class User_Serializer(ModelSerializer):

    class Meta:
        model = userDetails
        exclude = ['refreshToken', 'password']