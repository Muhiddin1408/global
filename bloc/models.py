import uuid
from account.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.


class Product(models.Model):
    PRODUCT_TYPE = (
        ('furniture', 'FURNITURE'),
        ('phones', 'PHONES'),
        ('accessories', 'ACCESSORIES')
    )
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1024, blank=True, null=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='product/', blank=True, null=True)
    type = models.CharField(choices=PRODUCT_TYPE, max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    ORDER_STATUS_CHOICES = (
        ('pending', 'PENDING'),
        ('delivering', 'DELIVERING'),
        ('completed', 'COMPLETED'),
        ('not cancelled', 'NOT CANCELLED'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    address = models.TextField(default='')
    status = models.CharField(choices=ORDER_STATUS_CHOICES, max_length=16, default='pending')
    products = models.TextField(default='')
    quantity = models.FloatField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.address


class OrderDetail(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self):
        return f'{self.id}'


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField(default=1)
    subtotel = models.FloatField(default=1)

    def __str__(self):
        return self.product


class Statistics(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.name
