from rest_framework.response import Response
from django.http import JsonResponse
from django.conf import settings
import cloudinary, pathlib

def try_catch_wrapper(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error Occuered: {str(e)}")
            return Response({"Error": str(e)})
    return wrapper



def cloudinary_file_uploader_utility(localFilePath: str) -> bool:
    try:  
        # cloudinary_obj = cloudinary.config(url=f"{settings.CLOUDINARY_URL}")

        # print(cloudinary_obj, cloudinary_obj.__dir__, cloudinary_obj.__dict__)
        
        from cloudinary import uploader
        
        # import cloudinary.api

        # 1st check if file path exists or not
        # if it does not exist then throw error response no path exist
        # if it exists then check, whether a file is exists 
        # if yes then, pass that local file path to the uploader func as keyword value
        # when file uploaded successfully then delete that file from local path. and return a success response

        # if upload operation got interrupted or abort by any fault
        # then remove that file from local path.
        # and ask user to try again to upload the file

        if not localFilePath or localFilePath is None:
            print("throw error that file path does not exist")
            return False

        data = uploader.upload(
            # file="https://upload.wikimedia.org/wikipedia/commons/a/ae/Olympic_flag.jpg",
            # public_id = "olympic flag image"

            file = localFilePath,
            public_id = "a temp file"
        )

        print(data)

        pathlib.Path(localFilePath).unlink()

        return True, data['secure_url']

    except Exception as e:
        print(f"Error while uploading file on Cloudinary: {str(e)}")



class ApiError(Response): # custom class for error responses

    def __init__(
            self, 
            data={"error": "something went wrong"}, 
            status=400, 
            template_name=None, 
            headers=None, 
            exception=False, 
            content_type=None
        ):
        return super().__init__(data, status, template_name, headers, exception, content_type)



class ApiResponse(Response): # custom class for success responses

    def __init__(
            self, 
            data={"success": "Task completed"}, 
            status=200, 
            template_name=None, 
            headers=None, 
            exception=False, 
            content_type=None
        ):
        return super().__init__(data, status, template_name, headers, exception, content_type)