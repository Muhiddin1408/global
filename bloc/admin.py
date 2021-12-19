from django.contrib import admin
from .models import Category, Jihozlar, Post, SendMessage, Buy

# Register your models here.

admin.site.register(Category)
admin.site.register(Jihozlar)
admin.site.register(Post)
admin.site.register(SendMessage)
admin.site.register(Buy)
