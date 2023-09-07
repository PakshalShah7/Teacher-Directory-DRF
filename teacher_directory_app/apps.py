""" This file is created to help the teacher_directory_app include any application configuration for the app. """

from django.apps import AppConfig


class TeacherDirectoryAppConfig(AppConfig):
    """
    This class representing a Django application and its configuration.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'teacher_directory_app'
