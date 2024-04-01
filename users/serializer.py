from rest_framework import serializers
from .models import *
from rest_framework_mongoengine import serializers

class User_Serializer(serializers.DocumentSerializer):

    class Meta:
        model = userDetails
        exclude = ['refreshtoken', 'password']
        # field = '__all__'
    

    def validate(self, validated_data):
        print("i am in validate func to serializer")
        print(validated_data)
        
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
    

    def create(self, validated_data):
        print(" i am in serializer create func")
        user = userDetails.objects.create(
            username = validated_data.get("username"),
            fullname = validated_data.get("fullname"),
            email = validated_data.get("email"),
        )

        user.set_password(validated_data.get("password"))
        user.save()


class UserLoginSerializer(User_Serializer):

    class Meta:
        model = userDetails
        exclude = ['refreshtoken', 'password']


class UserSignupSerializer(User_Serializer):
    
    class Meta:
        model = userDetails
        fields = "__all__"
    
    def validate(self, validated_data):
        return super().validate(validated_data)
    

    def create(self, validated_data):
        print(" i am in serializer create func of usersignup serializer")

        user: userDetails = userDetails.objects.create(
            username = validated_data.get("username"),
            fullname = validated_data.get("fullname"),
            email = validated_data.get("email"),
            password = userDetails.set_password(validated_data.get("password"))
        )
        print("doing a password set for the user")
        # user.set_password(validated_data.get("password"))
        user.save()
        print("user saved successfully")
        return user