from django.conf import settings
from django.core.files.uploadedfile import UploadedFile
from rest_framework.response import Response
from .utils import ApiError
import functools


class fileUploadToLocalPath:
    def __init__(self, get_response) -> None:
        self.get_response = get_response
        print("i am in file upload middleware init func")
    
    

    def __call__(self, request):
        try:
            print("i am in file upload middleware call func")

            fetch_file = request.FILES['file']

            if not fetch_file:
                print("no file fetched")
                return ApiError({'error': 'file format found'})

            
            if not fetch_file.name.endswith((".jpg", ".png")):
                return ApiError({'error': 'file format not accepted'})


            with open(f"{settings.TEMP_MEDIA_UPLOAD_PATH}/{fetch_file.name}", "wb") as file:
                for chunk in fetch_file.chunks():
                    file.write(chunk)


            response = self.get_response(request)

            return response
        
        except Exception as e:
            print(f"Error while uploading file to local path")


def file_upload_middleware(func):
    print(func)

    @functools.wraps(func)
    def middleware(request, *args, **kwargs):
        try:
            print("i am in file upload middleware")

            fetch_file = request.request.FILES['file']
            print(fetch_file, fetch_file.name)

            if not fetch_file:
                print("no file fetched")
                return ApiError({'error': 'file format not found'})

            if not fetch_file.name.endswith((".jpg", ".png")):
                return ApiError({'error': 'file format not accepted'})

            # UploadedFile(file=fetch_file)

            with open(f"{settings.TEMP_MEDIA_UPLOAD_PATH}/{fetch_file.name}", "wb") as file:
                for chunk in fetch_file.chunks():
                    file.write(chunk)
                    
            print("file uploaded successfully in middleware")
            return func(request, *args, **kwargs)

            # return Response(response)
        
        except Exception as e:
            print(f"Error while uploading file to local path: {e}")
        
    return middleware