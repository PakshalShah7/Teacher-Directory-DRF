""" This file contains subject and teacher model. """

from django.db import models


class Subject(models.Model):
    """
    This model will store subject details.
    """
    name = models.CharField(max_length=30)

    def __str__(self):
        """
        The method allows us to convert an object into a string representation.
        """
        return self.name


class Teacher(models.Model):
    """
    This model will store teacher details.
    """
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    profile_image = models.ImageField(upload_to="profile_images/",
                                      default='profile_images/default_image.jpg')
    email_address = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    room_number = models.CharField(max_length=10)
    subject_taught = models.ManyToManyField(Subject)

    def __str__(self):
        """
        The method allows us to convert an object into a string representation.
        """
        return f"First Name: {self.first_name} Last Name: {self.last_name}"
