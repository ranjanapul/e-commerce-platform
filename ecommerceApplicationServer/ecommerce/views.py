from traceback import print_exception
from .serializers import UserSerializer, ProductSerializer, OrderSerializer
from .tokenExtractor import getToken
from django.http import Http404, JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from.models import Product, Order



class UserDetailsView(APIView):

    def getUserObject(self, userId):  # Not predefined in APIView class
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

        user = self.getUserObject(userId)
        print(user.userType)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Get details of all products.


class ProductView(APIView):

    def getUserObject(self, userId):  # Not predefined in APIView class
        try:
            return User.objects.get(userId=userId)
        except User.DoesNotExist:
            raise Http404
# Vendor cannot see all products. So, need to create separate API for vendor products
    def get(self, request, format=None):
        try:
            userId = getToken(request)
        except Exception:
            return Response(
                {"message": "invalid token provided."},
                status=status.HTTP_401_UNAUTHORIZED)

        user = self.getUserObject(userId)
        if user.userType =='Customer':
            productList = Product.objects.all()
            serializer = ProductSerializer(productList, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            productList = Product.objects.all().filter(vendorId=user.userId)
            serializer = ProductSerializer(productList, many=True)
            return JsonResponse(serializer.data, safe=False)
            
    
    def post(self, request, *args, **kwargs):
        try:
            userId = getToken(request)
        except Exception:
            return Response(
                {"message": "invalid token provided."},
                status=status.HTTP_401_UNAUTHORIZED)

        user = self.getUserObject(userId)
        if user.userType =='Vendor':
            productData = request.data

            newProduct = Product.objects.create(
                vendorId = user.userId,
                productName = productData["productName"],
                productImageURL = productData["productImageURL"],
                price = productData["price"],
                productQuantity = productData["productQuantity"],
                productDescription = productData["productDescription"],
                productUnit = productData["productUnit"],
                productStatus = productData["productStatus"])
                
            newProduct.save()
            serializer = ProductSerializer(newProduct)
            return JsonResponse(serializer.data)
        else:
            return Response(
                {"message": "invalid token provided."},
                status=status.HTTP_401_UNAUTHORIZED)


class ProductDetailsView(APIView):

    def getUserObject(self, userId):  # Not predefined in APIView class
        try:
            return User.objects.get(userId=userId)
        except User.DoesNotExist:
            raise Http404



    def get(self, request, productId, format=None):
        product = Product.objects.get(productId=productId)
        serializer = ProductSerializer(product)
        return JsonResponse(serializer.data)

    def patch(self,request,productId,format=None):
        try:
            userId = getToken(request)
        except Exception:
            return Response(
                {"message": "invalid token provided."},
                status=status.HTTP_401_UNAUTHORIZED)
        user = self.getUserObject(userId)
        product = Product.objects.get(productId=productId)
        if user.userType == 'Vendor' and product.vendorId == user.userId:
            data=request.data
            product.productName = data.get("productName",product.productName)
            product.productImageURL = data.get("productImageURL",product.productImageURL)
            product.price = data.get("price",product.price)
            product.productQuantity = data.get("productQuantity",product.productQuantity)
            product.productDescription = data.get("productDescription",product.productDescription)
            product.productUnit  = data.get("productUnit",product.productUnit)
            product.save()
            serializer = ProductSerializer(product)
            return JsonResponse(serializer.data)
        
        else:
            return Response(
                {"message": "invalid token provided."},
                status=status.HTTP_401_UNAUTHORIZED)            
             
    def delete(self,request,productId,format=None):
        try:
            userId = getToken(request)
        except Exception:
            return Response(
                {"message": "invalid token provided."},
                status=status.HTTP_401_UNAUTHORIZED)
        user = self.getUserObject(userId)
        product = Product.objects.get(productId=productId)
        if user.userType == 'Vendor' and product.vendorId == user.userId:
            data=request.data
            product.productStatus = data.get("productStatus",product.productStatus)
            product.save()
            serializer = ProductSerializer(product)
            return JsonResponse(serializer.data)
        else:
            return Response(
                {"message": "invalid token provided."},
                status=status.HTTP_401_UNAUTHORIZED)     



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
# Need to reduce quantity but will be done in later phase.
    def post(self, request, *args, **kwargs):
    
        try:
            userId = getToken(request)
        except Exception:
            return Response(
                {"message": "invalid token provided."},
                status=status.HTTP_401_UNAUTHORIZED)

        user = self.getUserObject(userId)
        if user.userType=='Customer':
            orderData = request.data
            product = Product.objects.get(productId=orderData['productId'])
            if (user.balance >= product.price * orderData['orderedProductQuantity'] 
                and orderData['orderedProductQuantity'] <= product.productQuantity):
                newOrder = Order.objects.create(
                    productId = orderData["productId"],
                    customerId = user.userId,
                    vendorId = product.vendorId,
                    orderNumber = orderData["orderNumber"],
                    orderedProductQuantity = orderData["orderedProductQuantity"],
                    orderedProductUnits = product.productUnit,
                    status = "In process"
                )
                newOrder.save()
                serializer = OrderSerializer(newOrder)
                return JsonResponse(serializer.data)
            
            elif user.balance < product.price * orderData['orderedProductQuantity']:
                return Response(
                    {"message": "Insufficient Balance"},
                    status=status.HTTP_404_NOT_FOUND
                )
            
            else:
                return Response(
                    {"message": "Out of Stock"},
                    status=status.HTTP_404_NOT_FOUND
                )
        else:
            return Response(
                {"message": "invalid token provided."},
                status=status.HTTP_401_UNAUTHORIZED) 

class OrderDetailsView(APIView):

    def getUserObject(self, userId):  # Not predefined in APIView class
        try:
            return User.objects.get(userId=userId)
        except User.DoesNotExist:
            raise Http404

    def patch(self,request,orderId,format=None):
        try:
            userId = getToken(request)
        except Exception:
            return Response(
                {"message": "invalid token provided."},
                status=status.HTTP_401_UNAUTHORIZED)
        user = self.getUserObject(userId)
        order = Order.objects.get(orderId=orderId)
        if user.userType == 'Vendor' and order.vendorId == user.userId:
            data = request.data
            if data.get("status", order.status) == 'Delivered':
                order.status = data.get("status", order.status)
                order.save()
                serializer = OrderSerializer(order)
                return JsonResponse(serializer.data)
            else:
                return Response(
                    {"message": "Bad request"},
                    status=status.HTTP_404_NOT_FOUND
                )

        elif ((user.userType == 'Vendor' and order.vendorId == user.userId) or (user.userType == 'Customer' and order.customerId == user.userId)):
            # Vendor cant cancel order yet
            data = request.data
            if data.get("status", order.status) == 'Cancelled':
                order.status = data.get("status", order.status)
                order.save()
                serializer = OrderSerializer(order)
                return JsonResponse(serializer.data)
            else:
                return Response(
                    {"message": "Bad request"},
                    status=status.HTTP_404_NOT_FOUND
            )
        else:
            return Response(
                {"message": "invalid token provided."},
                status=status.HTTP_401_UNAUTHORIZED)





 