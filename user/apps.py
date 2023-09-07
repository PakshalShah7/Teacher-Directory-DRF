""" This file is created to help the user include any application configuration for the app. """

from django.apps import AppConfig


class UserConfig(AppConfig):
    """
    This class representing a Django application and its configuration.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'
