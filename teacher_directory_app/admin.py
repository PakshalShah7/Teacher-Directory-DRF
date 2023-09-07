""" This file registers subject and teacher model in admin site. """

from django.contrib import admin
from teacher_directory_app.models import Subject, Teacher


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    """
    This class will register subject model in admin site.
    """
    list_display = ['name']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    """
    This class will register teacher model in admin site.
    """
    list_display = ['first_name', 'last_name']
