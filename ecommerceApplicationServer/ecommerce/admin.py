from django.contrib import admin
from .models import User
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['userId', 'userType', 'name', 'address', 'phoneNumber',
                    'email', 'status', 'createdTs']
