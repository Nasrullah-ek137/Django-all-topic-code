from django.apps import AppConfig


class Shanuapp1Config(AppConfig):
    #default_auto_field = 'django.db.models.BigAutoField'
    name = 'shanuapp1'

    def ready(self):
        import shanuapp1.signals
