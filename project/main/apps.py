# Файл для конфигурации приложения!
from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main' # В идеальном пире название приложеня совпадает с названием директории!
