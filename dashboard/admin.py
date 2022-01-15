from django.contrib import admin
from .models import Club
# Register your models here.


class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'money')
    change_list_template = 'dashboard/template/chart_admin.html'

admin.site.register(Club, ClubAdmin)
