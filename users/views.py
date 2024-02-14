from django.shortcuts import render
from django.conf import settings

# Create your views here.

print(settings.SECRET_KEY)
print(settings.DEBUG)
print(settings.MONGODB_URI)