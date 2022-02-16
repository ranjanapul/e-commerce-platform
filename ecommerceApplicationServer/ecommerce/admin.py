from django.contrib import admin
from .models import User
from .models import Product
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['userId', 'userType', 'name', 'address', 'phoneNumber',
                    'email', 'status', 'createdTs']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['productId','vendorId', 'productName', 'productImageURL', 'price',
                    'productQuantity', 'productDescription', 'productUnit', 'productStatus',
                    'createdTs']
