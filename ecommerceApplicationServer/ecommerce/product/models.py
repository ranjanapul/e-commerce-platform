from django.db import models
from datetime import datetime
from django.core.validators import MinLengthValidator


class Product(models.Model):
    productId = models.AutoField(primary_key=True)
    vendorId = models.IntegerField(null=True)
    productName = models.CharField(max_length=30)
    productImageURL = models.CharField(max_length=80)
    price = models.IntegerField()
    productQuantity = models.IntegerField()
    productDescription = models.CharField(max_length=100)
    productUnit = models.CharField(max_length=20)
    productStatus = models.BooleanField()
    createdTs = models.DateTimeField(default=datetime.now, blank=True)

