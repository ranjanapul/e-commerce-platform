from django.db import models
from datetime import datetime
from django.core.validators import MinLengthValidator

class Order(models.Model):
    orderId = models.AutoField(primary_key=True)
    productId = models.IntegerField()
    customerId = models.IntegerField()
    vendorId = models.IntegerField()
    orderNumber = models.IntegerField()
    orderedProductQuantity = models.IntegerField()
    orderedProductUnits = models.IntegerField()
    IN_PROCESS = 'In process'
    DELIVERED = 'Delivered'
    CANCELLED = 'Cancelled'
    CHOICES = ((IN_PROCESS,'In process'), (DELIVERED,'Delivered'), (CANCELLED,'Cancelled'))
    status = models.CharField(max_length=15,choices=CHOICES)
    createdTs = models.DateTimeField(default=datetime.now, blank=True)
