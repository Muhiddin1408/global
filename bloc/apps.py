from django.apps import AppConfig
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class BlocConfig(AppConfig):
    name = 'bloc'

    def ready(self):
        import bloc.signal
