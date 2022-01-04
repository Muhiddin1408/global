from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    phone = models.CharField(max_length=12, default='')

    def __str__(self):
        return self.username

