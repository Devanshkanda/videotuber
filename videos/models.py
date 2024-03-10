from mongoengine import *
from users.models import userDetails
import datetime
# Create your models here.


class videos(Document):
    video_title = StringField(max_length=50, required=True)
    thumbnail = StringField() # url of file stored on cloudinary
    video_file = StringField() # url of file stored on cloudinary
    desc = StringField(default=f"{video_title}")
    duration = IntField(default=0)
    views = IntField(defualt=0)
    isPublished = BooleanField(default=False)
    owner = ReferenceField(userDetails, reverse_delete_rule=CASCADE) # a foreign key refering to userDetails table
    created_at = DateTimeField(default=datetime.datetime.utcnow())
    updated_at = DateTimeField(default=datetime.datetime.utcnow())