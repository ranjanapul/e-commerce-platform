from rest_framework import serializers
from datetime import datetime
from django.core.validators import MinLengthValidator


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