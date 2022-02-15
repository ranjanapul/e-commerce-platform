from rest_framework import serializers
from datetime import datetime
from django.core.validators import MinLengthValidator


class UserSerializer(serializers.Serializer):
    # userId = serializers.AutoField(primary_key=True)
    #CUSTOMER = 'Customer'
    #VENDOR = 'Vendor'
    #CHOICES = ((CUSTOMER, 'Customer'), (VENDOR, 'Vendor'))
    userType = serializers.CharField(max_length=10)
    name = serializers.CharField(max_length=40)
    address = serializers.CharField(max_length=100)
    phoneNumber = serializers.CharField(max_length=10,
                                   validators=[MinLengthValidator(10)])
    email = serializers.CharField(max_length=30)
    status = serializers.BooleanField()
    createdTs = serializers.DateTimeField(default=datetime.now)
    # modifiedTs = serializers.DateTimeField(auto_now=True)
    # , choices=CHOICES
    #, blank=True