from .utils import try_catch_wrapper, ApiError, ApiResponse, cloudinary_file_uploader_utility
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import permissions
from django.conf import settings
from .middleware import fileUploadToLocalPath, file_upload_middleware
from .models import *
from .serializer import User_Serializer
import pathlib
# Create your views here.


class userViewSet(ModelViewSet):
    queryset = userDetails.objects.all()
    serializer_class = User_Serializer
    permission_classes = [permissions.AllowAny]

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
        serialize = User_Serializer(data=data)

        if serialize.is_valid():
            serialize.save()

            return ApiResponse({
                "success": "user details saved and created successfully"
            }, status=201)
        
        return ApiError({
            "error": "failed to save user details. try again",
            "errpr details": serialize.errors
        }, status=400)


    @file_upload_middleware
    @action(detail=False, methods=['POST'])
    def uploadAvatar(self, request):

        data_and_file = request.data

        print(data_and_file['A file'])

        file_name = data_and_file['A file'].name

        if not pathlib.Path(f"{settings.TEMP_MEDIA_UPLOAD_PATH}/{file_name}").exists():
            return ApiError({
                "error": "file upload failed"
            }, status=500)
        

        upload_res, secure_url = cloudinary_file_uploader_utility(f"{settings.TEMP_MEDIA_UPLOAD_PATH}/{file_name}")


        if not upload_res:
            return ApiError({
                "error": "file upload failed"
            }, status=500)
        

        return ApiResponse(
            data={
                'success': "file uploaded successfully",
                "file url": secure_url
            },
            status=201
        )