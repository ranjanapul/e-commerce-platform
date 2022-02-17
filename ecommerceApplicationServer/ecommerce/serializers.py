from rest_framework import serializers
from datetime import datetime
from django.core.validators import MinLengthValidator


class UserSerializer(serializers.Serializer):
    userType = serializers.CharField(max_length=10)
    name = serializers.CharField(max_length=40)
    address = serializers.CharField(max_length=100)
    phoneNumber = serializers.CharField(max_length=10,
                                        validators=[MinLengthValidator(10)])
    email = serializers.CharField(max_length=30)
    balance= serializers.IntegerField()
    status = serializers.BooleanField()
    createdTs = serializers.DateTimeField(default=datetime.now)


class ProductSerializer(serializers.Serializer):
    vendorId=serializers.IntegerField()
    productName = serializers.CharField(max_length=30)
    productImageURL = serializers.CharField(max_length=80)
    price = serializers.IntegerField()
    productQuantity = serializers.IntegerField()
    productDescription = serializers.CharField(max_length=100)
    productUnit = serializers.CharField(max_length=20)
    productStatus = serializers.BooleanField()
    createdTs = serializers.DateTimeField(default=datetime.now)

class OrderSerializer(serializers.Serializer):
    productId = serializers.IntegerField()
    customerId = serializers.IntegerField()
    vendorId = serializers.IntegerField()
    orderNumber = serializers.IntegerField()
    orderedProductQuantity = serializers.IntegerField()
    orderedProductUnits = serializers.CharField(max_length=10)
    status = serializers.CharField(max_length=15)
    createdTs = serializers.DateTimeField(default=datetime.now)

class ReviewSerializer(serializers.Serializer):
    userId = serializers.IntegerField()
    orderId = serializers.IntegerField()
    productId = serializers.IntegerField()
    comment = serializers.CharField(max_length=150)
    rating = serializers.IntegerField()
    status = serializers.BooleanField()
    createdTs = serializers.DateTimeField(default=datetime.now)