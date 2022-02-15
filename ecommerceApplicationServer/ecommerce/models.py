from django.db import models
from datetime import datetime
from django.core.validators import MinLengthValidator


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
    status = models.BooleanField()
    createdTs = models.DateTimeField(default=datetime.now, blank=True)
    # modifiedTs = models.DateTimeField(auto_now=True)
