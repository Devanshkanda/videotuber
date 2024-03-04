from .utils import try_catch_wrapper, ApiError, ApiResponse
from .models import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
# Create your views here.


@try_catch_wrapper
@api_view(["GET", "POST"])
@permission_classes([permissions.AllowAny])
def get_details(request):
    if request.method == "POST":
        data = request.data

        print(data)
        u1 = userDetails(**data)
        u1.insert_details()

        return ApiResponse({
            "success": "data inserted successfully bro"
        },status=200)
        # return ApiError({"error": "this method request is not allowed"}, status=401)
    

    elif request.method == "GET":
        try:
            print("i am in get request if block")

            context = userDetails.fetch_all_details()

            return ApiResponse({
                "success": "Fetch all the details of all the users",
                "data": context
            }, status=200)
        except Exception as e:
            return ApiError({"error": "error a gaya"})
        

    else:
        return ApiError({"error": "kuch galat ho gaya bhai"})