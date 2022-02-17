from django.contrib import admin
from .models import User
from .models import Product
from .models import Order, Review
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['userId', 'userType', 'name', 'address', 'phoneNumber',
                    'email','balance', 'status', 'createdTs']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['productId','vendorId', 'productName', 'productImageURL', 'price',
                    'productQuantity', 'productDescription', 'productUnit', 'productStatus',
                    'createdTs']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['orderId', 'productId', 'customerId', 'vendorId', 'orderNumber',
                    'orderedProductQuantity','orderedProductUnits','status', 'createdTs']

@admin.register(Review)
class ReviewAdmin(Review):
    list_display = ['reviewId', 'userId', 'orderId', 'productId', 'comment', 'rating', 
                    'status', 'createdTs']


