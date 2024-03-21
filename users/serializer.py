from rest_framework import serializers
from .models import *
from rest_framework_mongoengine import serializers

class User_Serializer(serializers.DocumentSerializer):

    class Meta:
        model = userDetails
        exclude = ['refreshtoken', 'password']
        # field = '__all__'
    

    def validate(self, validated_data):
        
        username: str = validated_data.get('username')
        password: str = validated_data.get('password')
        email: str = validated_data.get('email')
        fullname: str = validated_data.get('fullname')

        if not username:
            raise ValidationError("No username entered. please enter a username")
        
        if not password:
            raise ValidationError("no password entered. please set a password")
        
        if not email:
            raise ValidationError("email not entered. email is required")
        
        if not fullname:
            raise ValidationError("fullname not entered. fullname is required")
        

        return validated_data