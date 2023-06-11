from django.apps import AppConfig


class CustomizationAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customization_app'
