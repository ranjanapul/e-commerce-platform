from .serializers import UserSerializer, ProductSerializer
from .tokenExtractor import getToken
from django.http import Http404, JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from.models import Product


class UserDetailsView(APIView):

    def get_object(self, userId):  # Not predefined in APIView class
        try:
            return User.objects.get(userId=userId)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, format=None):  # gets invoked if GET request is done
        try:
            userId = getToken(request)
        except Exception:
            return Response(
                {"message": "invalid token provided."},
                status=status.HTTP_401_UNAUTHORIZED)

        user = self.get_object(userId)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Get details of all products.


class ProductDetailsView(APIView):

    def get_object(self, userId):  # Not predefined in APIView class
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
        user = self.get_object(userId)
        if user is not None:
            try:  # if productId is not None ie present in db this block is executed.
                productId = request.query_params['productId']
                product = Product.objects.get(productId=productId)
                serializer = ProductSerializer(product)
                return JsonResponse(serializer.data)

            except Exception:# Exception is raised if no product id is provided. In that case, return all products.
                productList = Product.objects.all()
                serializer = ProductSerializer(productList, many=True)
                return JsonResponse(serializer.data, safe=False)


