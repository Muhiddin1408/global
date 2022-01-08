from django.apps import AppConfig


class BlocConfig(AppConfig):
    name = 'bloc'

    def ready(self):
        import bloc.signal
