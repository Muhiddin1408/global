import uuid
from account.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.



# class SendMessage(models.Model):
#     title = models.CharField(max_length=100, default='')
#     name = models.CharField(max_length=64)
#     number = models.IntegerField(default=1)
#     email = models.EmailField(max_length=256, blank=True, null=True)
#     phone_number = models.CharField(max_length=12)
#     price = models.IntegerField(default=0)
#
#
#     def __str__(self):
#         return self.name


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
    image = models.ImageField(upload_to='product/', blank=True, null=True)
    type = models.CharField(choices=PRODUCT_TYPE, max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    address = models.TextField(default='')
    status = models.CharField(choices=ORDER_STATUS_CHOICES, max_length=16, default='pending')
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
        return self.user.username


