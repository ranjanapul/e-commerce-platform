from traceback import print_exception
from ecommerce.tokenExtractor import getToken
from django.http import Http404, JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ecommerce.models import User
from ecommerce.product.models import Product
from .models import Order
from .serializers import OrderSerializer


class OrderView(APIView):
    
    def getUserObject(self, userId):  # Not predefined in APIView class
        try:
            return User.objects.get(userId=userId)
        except User.DoesNotExist:
            raise Http404
    
    def get(self, request, format=None):
        try:
            userId = getToken(request)
        except Exception:
            return Response(
                {"message": "invalid token provided."},
                status=status.HTTP_401_UNAUTHORIZED)
        user = self.getUserObject(userId)
        if user.userType =='Vendor':
            orderList = Order.objects.all().filter(vendorId=user.userId)
            serializer = OrderSerializer(orderList, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            orderList = Order.objects.all().filter(customerId=user.userId)
            serializer = OrderSerializer(orderList, many=True)
            return JsonResponse(serializer.data, safe=False)
            




    