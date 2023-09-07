""" This file contains factories of subject and teacher model. """

import factory.django
from factory import Faker
from factory.django import DjangoModelFactory
from teacher_directory_app.models import Subject, Teacher


class SubjectFactory(DjangoModelFactory):
    """
    This class will create factory which will generate data for subject model.
    """
    name = Faker("name")

    class Meta:
        """
        Model Meta is basically the inner class of your model class.
        Model Meta is basically used to change the behavior of your model fields like changing
        order options,verbose_name, and a lot of other options.
        """
        model = Subject


class TeacherFactory(DjangoModelFactory):
    """
    This class will create factory which will generate data for teacher model.
    """
    first_name = Faker("name")
    last_name = Faker("name")
    profile_image = factory.django.ImageField(upload_to='profile_images/')
    email_address = Faker("name")
    phone_number = Faker("phone_number", locale='hi_IN')
    room_number = Faker("name")

    @factory.post_generation
    def subject_taught(self, create, extracted):
        """
        This class should create factory for subject model.
        """
        if not create:
            return

        if extracted:
            for subject in extracted:
                self.subject_taught.add(subject)

    class Meta:
        """
        Model Meta is basically the inner class of your model class.
        Model Meta is basically used to change the behavior of your model fields like changing
        order options,verbose_name, and a lot of other options.
        """
        model = Teacher
