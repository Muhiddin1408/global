from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from account.models import User


UserAdmin.fieldsets += (
    (None, {'fields': ('phone', )}),
)

admin.site.register(User, UserAdmin)
