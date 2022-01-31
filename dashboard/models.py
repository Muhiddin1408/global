from django.db import models

# Create your models here.


class RoleModuleConfiguration(models.Model):
    posts = models.BooleanField(default=True)
    users = models.BooleanField(default=True)
    role_name = models.CharField(max_length=255)