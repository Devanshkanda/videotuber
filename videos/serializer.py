from rest_framework.serializers import ModelSerializer
from .models import *


class Videos_Serializer(ModelSerializer):

    class Meta:
        model = videos
        fields = '__all__'