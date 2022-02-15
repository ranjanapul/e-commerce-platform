from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from .tokenExtractor import *
# Create your views here.
#Model Object- Single User Data
def user_detail(request):
    userId= getToken(request)
    # print(request.headers['HTTP_AUTHORIZATION'])
    user=User.objects.get(userId=userId)
    serializer=UserSerializer(user)
    return JsonResponse(serializer.data)




