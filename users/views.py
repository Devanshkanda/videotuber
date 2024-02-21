from django.shortcuts import render
from django.conf import settings
from .utils import try_catch_wrapper
from .models import *
from django.http import JsonResponse
# Create your views here.


@try_catch_wrapper
def get_details(request):
    if request.method == "GET":
        data = request.data

        u1 = userDetails(**data)
        u1.insert_details()

        return JsonResponse({
            "success": "data inserted successfully bro"
        })
    else:
        return JsonResponse({"error": "this method request is not allowed"})