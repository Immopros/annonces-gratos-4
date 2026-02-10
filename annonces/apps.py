from django.apps import AppConfig

class AnnoncesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'annonces'

    def ready(self):
        from .create_admin import create_superuser
        create_superuser()
