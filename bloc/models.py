import uuid

from django.db import models
# Create your models here.


class SendMessage(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=64)
    number = models.IntegerField(default=1)
    email = models.EmailField(max_length=256, blank=True, null=True)
    phone_number = models.CharField(max_length=12)
    price = models.IntegerField(default=0)


    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, verbose_name='Url', unique=True, default=uuid.uuid4)
    content = models.TextField()
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Jihozlar(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, verbose_name='Url', unique=True, default=uuid.uuid4)
    photo = models.ImageField(upload_to='media')
    description = models.TextField(default='')
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='media', null=True, blank=True)
    user_name = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='опубликовано')
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Buy(models.Model):
    title = models.ForeignKey(Jihozlar, on_delete=models.CASCADE)
    price = models.IntegerField()
    number = models.IntegerField(default=1)
    phone_number = models.CharField(max_length=12)
    name = models.CharField(max_length=64)
