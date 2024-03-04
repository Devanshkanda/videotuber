
# try catch utility
from rest_framework.response import Response
from django.http import JsonResponse

def try_catch_wrapper(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error Occuered: {str(e)}")
            return Response({"Error": str(e)})
    return wrapper



class ApiError(Response): # custom class for error responses

    def __init__(self, data={"error": "something went wrong"}, status=400, template_name=None, headers=None, exception=False, content_type=None):
        super().__init__(data, status, template_name, headers, exception, content_type)



class ApiResponse(Response): # custom class for success responses

    def __init__(self, data={"success": "Task completed"}, status=200, template_name=None, headers=None, exception=False, content_type=None):
        super().__init__(data, status, template_name, headers, exception, content_type)