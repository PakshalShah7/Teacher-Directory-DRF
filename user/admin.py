""" This file registers model in admin site. """

from django.contrib import admin
from user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    This class will register user model in admin site.
    """
    list_display = ['username']
