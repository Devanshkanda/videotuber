from mongoengine import *
from users.models import userDetails
import datetime
# Create your models here.


class videos(Document):
    video_title = StringField(max_length=50, required=True)
    thumbnail = StringField() # url of file stored on cloudinary
    video_file = StringField(required=True) # url of file stored on cloudinary
    desc = StringField(default=f"{video_title}")
    duration = IntField(default=0)
    views = IntField(defualt=0)
    isPublished = BooleanField(default=False)
    public = BooleanField(default=True) # setting video publicaly visible or not
    owner = ReferenceField(userDetails, reverse_delete_rule=CASCADE, dbref=True) # a foreign key refering to userDetails table
    created_at = DateTimeField(default=datetime.datetime.now(datetime.UTC))
    updated_at = DateTimeField(default=datetime.datetime.now(datetime.UTC))


    def set_duration(self):
        pass