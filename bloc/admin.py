from django.contrib import admin
# from django.contrib.auth.models import Group
from .models import Product, OrderDetail, Order, Cart, Statistics, Category

# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(OrderDetail)
admin.site.register(Statistics)
