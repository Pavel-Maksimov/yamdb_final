from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = 'api'
    models_module = 'api/models/'
