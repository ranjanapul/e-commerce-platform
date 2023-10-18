"""ecommerceApplicationServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ecommerce.views import UserDetailsView, ProductDetailsView, ProductView, OrderView, OrderDetailsView
from ecommerce.views import ReviewView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('user', UserDetailsView.as_view(), name='user'), # Name is used to refer to it on the frontend
    path('product', ProductView.as_view(), name='product'),
    path('product/<int:productId>', ProductDetailsView.as_view(), name='productDetails'),
    path('order', OrderView.as_view(), name= 'order'),
    path('order/<int:orderId>',OrderDetailsView.as_view(), name='orderDetails'),
    path('product/<int:productId>/review', ReviewView.as_view(), name='review'),
    # path('product/<int:productId>/review/<int:reviewId>'.ReviewDetailsView.as_view(), name='reviewDetails')
]
# About line 23: To use UserDetailsView class's functions.
# Like get() get invoked solely beacuse the type of request is GET
# Line 31: Coming soon