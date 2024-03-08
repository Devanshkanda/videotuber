from rest_framework.response import Response
from django.http import JsonResponse
from django.conf import settings
import cloudinary

def try_catch_wrapper(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error Occuered: {str(e)}")
            return Response({"Error": str(e)})
    return wrapper



def cloudinary_file_uploader_utility(filePath: str):
    try:  
        data = cloudinary.config(url=f"{settings.CLOUDINARY_URL}")

        print(data, data.__dir__, data.__dict__)
        
        # from cloudinary import uploader
        # import cloudinary.api

        # cloudinary.uploader.upload(
        #     "https://upload.wikimedia.org/wikipedia/commons/a/ae/Olympic_flag.jpg",
        #     public_id = "olympic_flag"
        # )

        # data = uploader.upload(
        #     file="https://upload.wikimedia.org/wikipedia/commons/a/ae/Olympic_flag.jpg",
        #     public_id = "olympic"
        # )


    except Exception as e:
        print(f"Error while uploading file on Cloudinary: {str(e)}")



class ApiError(Response): # custom class for error responses

    def __init__(self, data={"error": "something went wrong"}, status=400, template_name=None, headers=None, exception=False, content_type=None):
        super().__init__(data, status, template_name, headers, exception, content_type)



class ApiResponse(Response): # custom class for success responses

    def __init__(self, data={"success": "Task completed"}, status=200, template_name=None, headers=None, exception=False, content_type=None):
        super().__init__(data, status, template_name, headers, exception, content_type)