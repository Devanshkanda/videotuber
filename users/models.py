# from django.db import models
from django.conf import settings
import bson, datetime
from mongoengine import *
from .utils import try_catch_wrapper


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


class videos(Document):
    video_title = StringField(max_length=50, required=True)
    thumbnail = StringField() # url of file stored on cloudinary
    video_file = StringField() # url of file stored on cloudinary
    desc = StringField(default=f"{video_title}")
    duration = IntField(default=0)
    views = fields.Int64()
    isPublished = BooleanField(default=False)
    owner = ReferenceField(userDetails, reverse_delete_rule=CASCADE) # a foreign key refering to userDetails table
    created_at = DateTimeField(default=datetime.datetime.utcnow())
    updated_at = DateTimeField(default=datetime.datetime.utcnow())