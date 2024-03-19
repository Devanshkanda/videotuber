from rest_framework import serializers
from .models import *
# from rest_framework_mongoengine import serializers

class User_Serializer(serializers.ModelSerializer):

    class Meta:
        model = userDetails
        exclude = ['refreshtoken', 'password']
    

    def validate(self, attrs):
        return super().validate(attrs)