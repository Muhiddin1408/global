import uuid
from django.contrib.auth.models import User
from django.db import models
# Create your models here.



class SendMessage(models.Model):
    title = models.CharField(max_length=100, default='')
    name = models.CharField(max_length=64)
    number = models.IntegerField(default=1)
    email = models.EmailField(max_length=256, blank=True, null=True)
    phone_number = models.CharField(max_length=12)
    price = models.IntegerField(default=0)


    def __str__(self):
        return self.name


# class Category(models.Model):
#     title = models.CharField(max_length=100)
#     slug = models.SlugField(max_length=100, verbose_name='Url', unique=True, default=uuid.uuid4)
#     content = models.TextField()
#
#     def __str__(self):
#         return self.title


# class Jihozlar(models.Model):
#     title = models.CharField(max_length=100)
#     slug = models.SlugField(max_length=100, verbose_name='Url', unique=True, default=uuid.uuid4)
#     photo = models.ImageField(upload_to='media')
#     description = models.TextField(default='')
#     price = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.title


# class Post(models.Model):
#     title = models.CharField(max_length=100)
#     photo = models.ImageField(upload_to='media', null=True, blank=True)
#     user_name = models.CharField(max_length=25)
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name='опубликовано')
#     price = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.title


class Product(models.Model):
    PRODUCT_TYPE = (
        ('furniture', 'FURNITURE'),
        ('phones', 'PHONES'),
        ('accessories', 'ACCESSORIES')
    )
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1024, blank=True, null=True)
    price = models.FloatField()
    type = models.CharField(choices=PRODUCT_TYPE, max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# class Buy(models.Model):
#     title = models.ForeignKey(Jihozlar, on_delete=models.CASCADE)
#     price = models.IntegerField()
#     number = models.IntegerField(default=1)
#     phone_number = models.CharField(max_length=12)
#     name = models.CharField(max_length=64)


class Order(models.Model):
    ORDER_STATUS_CHOICES = (
        ('pending', 'PENDING'),
        ('delivering', 'DELIVERING'),
        ('completed', 'COMPLETED'),
        ('cancelled', 'CANCELLED'),
    )
    email = models.EmailField()
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=32)
    status = models.CharField(choices=ORDER_STATUS_CHOICES, max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return self.order.name


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)



