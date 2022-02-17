from rest_framework import serializers
from datetime import datetime


class OrderSerializer(serializers.Serializer):
    productId = serializers.IntegerField()
    customerId = serializers.IntegerField()
    vendorId = serializers.IntegerField()
    orderNumber = serializers.IntegerField()
    orderedProductQuantity = serializers.IntegerField()
    orderedProductUnits = serializers.IntegerField()
    status = serializers.CharField(max_length=15)
    createdTs = serializers.DateTimeField(default=datetime.now)
