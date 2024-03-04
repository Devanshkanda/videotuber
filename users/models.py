# from django.db import models
from django.conf import settings
import bson
from mongoengine import *
from .utils import try_catch_wrapper

# Create your models here.


# class userDetails:
#     collection = settings.DB['USERS']

#     def __init__(
#             self,
#             fullName: str = None,
#             username: str = None,
#             email: str = None,
#             password: str = None,
#             avatar: str = None,
#             coverImage: str = None,
#             refreshToken = None,
#             createdAt = None
#             ) -> None:
        
#         self.fullName = fullName
#         self.username = username
#         self.email = email
#         self.avatar = avatar
#         self.coverImage = coverImage
#         self.password = password
#         self.refreshToken = refreshToken
    

#     @try_catch_wrapper
#     def insert_details(self):
#         userDetails.collection.insert_one(self.__dict__)
#         print(f"Data inserted successfully")


#     @try_catch_wrapper
#     def fetch_all_details(self):
#         gett = userDetails.collection.find()
#         print(gett)
#         print("fetched all details successfully")
#         return gett
    

#     @try_catch_wrapper
#     def fetch_Details_By_Id(self, id):
#         userDetails.collection.find(bson.ObjectId(oid=id))
#         print(f"FEtched user details successfully by id {id}")
    

#     @try_catch_wrapper
#     def update_user_details(self, id, new_name):
#         userDetails.collection.update_one(
#             {"_id": bson.ObjectId(id)},
#             {"$set": {
#                 "name": new_name
#             }}
#         )
    
#     @try_catch_wrapper
#     def delete_video(self, id):
#         userDetails.collection.delete_one({"_id": bson.ObjectId(oid=id)})



import datetime

class userDetails(Document):
    username = StringField(max_length=20, required=True, unique=True)
    fullname = StringField(max_length=20, required=True)
    email = EmailField(required=True)
    password = StringField(required=True)
    avatar = StringField()
    coverImage = StringField()
    created_at = DateTimeField(default=datetime.datetime.utcnow())
    refreshtoken = StringField()