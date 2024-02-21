
# try catch utility
from django.http import JsonResponse

def try_catch_wrapper(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error Occuered: {str(e)}")
            return JsonResponse({"Error": str(e)})
    return wrapper
