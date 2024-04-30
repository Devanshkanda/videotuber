from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework_simplejwt.authentication import JWTStatelessUserAuthentication
from .models import *
from .serializer import *
from utils.utils import ApiError, ApiResponse
# Create your views here.


class VideosViewSet(viewsets.ModelViewSet):
    queryset = videos.objects.filter(public=True, isPublished=True)
    serializer_class = Get_Videos_Serializer
    permission_classes = [permissions.AllowAny]
    # authentication_classes = JWTStatelessUserAuthentication


    def list(self, request, *args, **kwargs):
        # return super().list(request, *args, **kwargs)
        return ApiResponse({
            "status": 200,
            "data": self.serializer_class(self.queryset, many=True).data,
        })
    
    def retrieve(self, request):
        return super().retrieve(request)
    
    def create(self, request, *args, **kwargs):
        return ApiError({"error": "Method not allowed"}, status=405)
    
    def update(self, request, *args, **kwargs):
        return ApiError({"error": "Method not allowed"}, status=405)
    
    def partial_update(self, request, *args, **kwargs):
        return ApiError({"error": "Method not allowed"}, status=405)
    
    def destroy(self, request, *args, **kwargs):
        return ApiError({"error": "Method not allowed"}, status=405)
    


    @action(methods=['POST'], detail=False, permission_classes=permission_classes)
    def createVideo(self, request):
        data = request.data
        serialize = Videos_Serializer(data=data)

        if serialize.is_valid():
            return ApiResponse({"message": "nice working"})
        else:
            return ApiError({"rror": "not working"})
