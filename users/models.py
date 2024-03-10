# from django.db import models
import datetime
from mongoengine import *


class userDetails(Document):
    username = StringField(max_length=20, required=True, unique=True)
    fullname = StringField(max_length=20, required=True)
    email = EmailField(required=True)
    password = StringField(required=True)
    avatar = StringField() # url of file stored on cloudinary
    coverImage = StringField() # url of file stored on cloudinary
    created_at = DateTimeField(default=datetime.datetime.utcnow())
    updated_at = DateTimeField(default=datetime.datetime.utcnow())
    refreshtoken = StringField()