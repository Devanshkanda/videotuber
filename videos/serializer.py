from rest_framework_mongoengine import serializers
from .models import *
from rest_framework_mongoengine.validators import ValidationError

class Videos_Serializer(serializers.DocumentSerializer):

    class Meta:
        model = videos
        fields = '__all__'
    

    def validate(self, validated_data):
        video_title: str = validated_data.get("title")

        if video_title == "T":
            raise ValidationError("invalid title name", 401)
        
        return validated_data
        

class Get_Videos_Serializer(serializers.DocumentSerializer):

    class Meta:
        model = videos
        exclude = ['isPublished', 'public', 'updated_at']