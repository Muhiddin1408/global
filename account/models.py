from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    status_choices = (
        ("true", "True"),
        ("false", "False"),
    )
    phone = models.CharField(max_length=12, default='')
    status = models.CharField(max_length=12, choices=status_choices, default='false')

    def __str__(self):
        return self.username

