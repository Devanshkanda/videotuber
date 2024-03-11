from django.conf import settings
from django.core.files.uploadedfile import UploadedFile


class fileUploadToLocalPath:
    def __init__(self, get_response) -> None:
        self.get_response = get_response
        print("i am in file upload middleware")
    

    def __call__(self, request):
        try:
            print("i am in file upload middleware")

            fetch_file = request.FILES['file']

            if not fetch_file:
                print("no file fetched")


            with open(f"{settings.TEMP_MEDIA_UPLOAD_PATH}/{fetch_file.name}", "wb") as file:
                for chunk in fetch_file.chunks():
                    file.write(chunk)


            response = self.get_response(request)

            return response
        
        except Exception as e:
            print(f"Error while uploading file to local path")


def file_upload_middleware(func):
    def wrapper(request):
        try:
            print("i am in file upload middleware")

            fetch_file = request.FILES['file']

            if not fetch_file:
                print("no file fetched")


            with open(f"{settings.TEMP_MEDIA_UPLOAD_PATH}/{fetch_file.name}", "wb") as file:
                for chunk in fetch_file.chunks():
                    file.write(chunk)


            response = func(request)

            return response
        
        except Exception as e:
            print(f"Error while uploading file to local path")
        
    return wrapper