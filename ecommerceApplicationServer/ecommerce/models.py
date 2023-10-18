from django.db import models
from datetime import datetime
from django.core.validators import MinLengthValidator
from django.forms import BooleanField


# Create your models here.
class User(models.Model):
    userId = models.AutoField(primary_key=True)
    CUSTOMER = 'Customer'
    VENDOR = 'Vendor'
    CHOICES = ((CUSTOMER, 'Customer'), (VENDOR, 'Vendor'))
    userType = models.CharField(max_length=10, choices=CHOICES)
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=10,
                                   validators=[MinLengthValidator(10)])
    email = models.CharField(max_length=30)
    balance = models.IntegerField()
    status = models.BooleanField()
    createdTs = models.DateTimeField(default=datetime.now, blank=True)
    # modifiedTs = models.DateTimeField(auto_now=True)


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

class Order(models.Model):
    orderId = models.AutoField(primary_key=True)
    productId = models.IntegerField()
    customerId = models.IntegerField()
    vendorId = models.IntegerField()
    orderNumber = models.IntegerField()
    orderedProductQuantity = models.IntegerField()
    orderedProductUnits = models.CharField(max_length=10)
    IN_PROCESS = 'In process'
    DELIVERED = 'Delivered'
    CANCELLED = 'Cancelled'
    CHOICES = ((IN_PROCESS,'In process'), (DELIVERED,'Delivered'), (CANCELLED,'Cancelled'))
    status = models.CharField(max_length=15,choices=CHOICES)
    createdTs = models.DateTimeField(default=datetime.now, blank=True)

class Review(models.Model):
    reviewId = models.AutoField(primary_key=True)
    userId = models.IntegerField()
    productId = models.IntegerField()
    comment = models.CharField(max_length=150)
    ONESTAR = 1
    TWOSTAR = 2
    THREESTAR = 3
    FOURSTAR = 4
    FIVESTAR = 5
    CHOICES = ((ONESTAR,1),(TWOSTAR,2),(THREESTAR,3),(FOURSTAR,4),(FIVESTAR,5))
    rating = models.IntegerField(choices=CHOICES)
    status = models.BooleanField()
    createdTs = models.DateTimeField(default=datetime.now, blank=True)
# test
# jgndfjonfdvjnsd