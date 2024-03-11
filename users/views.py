from .utils import try_catch_wrapper, ApiError, ApiResponse, cloudinary_file_uploader_utility
from .models import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import permissions
from django.conf import settings
from .middleware import fileUploadToLocalPath, file_upload_middleware
import pathlib
# Create your views here.


class userViewSet(ModelViewSet):
    # queryset = userDetails.objects.all()
    permission_classes = [permissions.AllowAny]

    @file_upload_middleware
    @action(detail=False, methods=['POST'])
    def test(self, request):

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