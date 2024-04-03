# from django.db import models
import datetime
from django.contrib.auth.hashers import check_password, BCryptSHA256PasswordHasher
import bcrypt
from mongoengine import *

class userDetails(Document):
    username = StringField(max_length=20, required=True, unique=True)
    fullname = StringField(max_length=20, required=True)
    email = EmailField(required=True)
    password = StringField(required=True)
    avatar = StringField() # url of file stored on cloudinary
    coverImage = StringField() # url of file stored on cloudinary
    created_at = DateTimeField(default=datetime.datetime.now(datetime.UTC))
    updated_at = DateTimeField(default=datetime.datetime.now(datetime.UTC))
    refreshtoken = StringField()


    def get_password(self) -> str:
        return self.password
    
    @staticmethod
    def set_password(plain_text: str) -> bytes:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password=plain_text.encode(), salt=salt)
        # self.password = hashed_password
        return hashed_password
    
    def validate_password(self, plain_text_password: str) -> bool:
        # return check_password(password=plain_text_password, encoded=self.password)
        return bcrypt.checkpw(plain_text_password.encode(), self.password.encode())