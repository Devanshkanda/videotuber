from utils.utils import (
    ApiError,
    ApiResponse,
    try_catch_wrapper,
    cloudinary_file_uploader_utility,
    generateAccessTokenAndRefreshToken
)

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import permissions, status
from rest_framework_simplejwt.authentication import JWTStatelessUserAuthentication
from django.conf import settings
from .middleware import file_upload_middleware
from .models import *
from .serializer import *
from mongoengine.queryset.visitor import Q as mongo_q
import pathlib
# Create your views here.


class userViewSet(ModelViewSet):
    queryset = userDetails.objects.all()
    serializer_class = User_Serializer
    permission_classes = [permissions.AllowAny]
    # authentication_classes = [JWTStatelessUserAuthentication]

    def create(self, request):
        # return super().create(request, *args, **kwargs)

        # get json data from request
        # will check for integrity constraints
        # check for required fields
        # if all is good and met then save data
        # generate token for that user
        # store refresh token for that user
        # return response to the user with its details , token , 
        # and unwanted info

        data = request.data
        print("i am in create func")
        print(request.user.id, request.auth)
        serialize = User_Serializer(data=data)

        if serialize.is_valid():
            serialize.save()

            return ApiResponse({
                "success": "user details saved and created successfully",
                "data": serialize.data
            }, status=status.HTTP_201_CREATED)
        
        return ApiError({
            "error": "failed to save user details. try again",
            "errpr details": serialize.errors
        }, status=status.HTTP_406_NOT_ACCEPTABLE)


    @action(detail=False, methods=['POST'])
    def signup(self, request):

        data = request.data
        print(data)
        serialize = UserSignupSerializer(data=data)

        if serialize.is_valid():
            user: userDetails = serialize.save()

            userdata = {
                "id": str(user.id),
                "username": str(user.username),
                "fullname": str(user.fullname),
            }
            
            return ApiResponse({
                "success": "user details saved and created successfully",
                "data": userdata
            }, status=status.HTTP_201_CREATED)
        
        return ApiError({
            "error": "failed to save user details. try again",
            "errpr details": serialize.errors
        }, status=status.HTTP_406_NOT_ACCEPTABLE)


    @action(detail=False, methods=['POST'])
    def login(self, request):
        # request.data -> data
        # username or email
        # find the user
        # password check
        # access token and refresh token
        # send cookies

        # if request.user is not "AnonymousUser" or request.auth is not None:
        #     return ApiError({
        #         "error": "user already logged in",
        #         "user": str(request.user),
        #         "auth": str(request.auth)
        #     }, status=400)
        
        
        username, email, password = request.data.values()
        print(username, email, password)

        if (not username and not email):
            return ApiError({
                "error": "username or Email is required"
            }, status=400)
        
        user: userDetails = userDetails.objects.filter(
            (mongo_q(username=username) | mongo_q(email=email))).first()
        print(user)

        if not user or user is None:
            return ApiError({
                "error": "no user found. incorrect username or password"
            }, status=400)
        
        # now validate password of the user

        if not user.validate_password(password):
            return ApiError({
                "error": "Invalid user credentials"
            }, status=401)
        
        # now we got the entry of the user in our database. now generate jwt tokens

        refreshtoken = generateAccessTokenAndRefreshToken(user)

        user.refreshtoken = str(refreshtoken)
        user.save()
        
        return ApiResponse({
            "success": "Logged in user successfully",
            "user": str(user.username),
            "refresh token": str(refreshtoken),
            "access Token": str(refreshtoken.access_token)
        })


    @action(detail=False, methods=['POST'])
    @file_upload_middleware
    def uploadAvatar(self, request):
        print("i am in upload avatar func")
        data_and_file = request.data

        print(data_and_file['file'])

        file_name = data_and_file['file'].name

        if not file_name:
            return ApiError({
                "error": "no avatar file found"
            }, status=400)

        if not pathlib.Path(f"{settings.TEMP_MEDIA_UPLOAD_PATH}/{file_name}").exists():
            return ApiError({
                "error": "file upload failed"
            }, status=500)
        

        localFilePath: str = f"{settings.TEMP_MEDIA_UPLOAD_PATH}/{file_name}"

        upload_res, secure_url = cloudinary_file_uploader_utility(localFilePath)


        if not upload_res:
            return ApiError({
                "error": "file upload failed"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
        # here i can now store the secure url of the file in the current user model object
        user = userDetails.objects.filter(id = request.user.id).first()

        if not user:
            return ApiError({
                "error": "no user found"
            })
        
        user.coverImage = secure_url
        user.save()

        return ApiResponse(
            data={
                'success': "Avatar Image uploaded successfully",
                "file url": secure_url
            },
            status=status.HTTP_201_CREATED
        )
    

    @action(detail=False, methods=['POST'])
    @file_upload_middleware
    def uploadCoverImage(self, request):

        print("i am in upload avatar func")
        data_and_file = request.data

        print(data_and_file['file'])

        file_name = data_and_file['file'].name

        if not file_name:
            return ApiError({
                "error": "no avatar file found"
            }, status=400)

        if not pathlib.Path(f"{settings.TEMP_MEDIA_UPLOAD_PATH}/{file_name}").exists():
            return ApiError({
                "error": "file upload failed"
            }, status=500)
        

        localFilePath: str = f"{settings.TEMP_MEDIA_UPLOAD_PATH}/{file_name}"

        upload_res, secure_url = cloudinary_file_uploader_utility(localFilePath)


        if not upload_res:
            return ApiError({
                "error": "file upload failed"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
        # here i can now store the secure url of the file in the current user model object
        user = userDetails.objects.filter(id = id).first()

        if not user:
            return ApiError({
                "error": "no user found"
            })
        
        user.coverImage = secure_url
        user.save()

        return ApiResponse(
            data={
                'success': "Cover Image uploaded successfully",
                "file url": secure_url
            },
            status=status.HTTP_201_CREATED
        )

# from django.http import JsonResponse

# def view1(request):
#     return JsonResponse({
#         "success": "i am view one"
#     })

# def view2(request):
#     return JsonResponse({
#         "success": "i am view 2"
#     })