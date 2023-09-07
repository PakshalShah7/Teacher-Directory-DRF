""" This file contains filter class for teacher model. """

from django_filters import FilterSet
from teacher_directory_app.models import Teacher


class TeacherFilter(FilterSet):
    """
    This class is filter class for teacher model.
    """

    class Meta:
        """
        Model Meta is basically the inner class of your model class.
        Model Meta is basically used to change the behavior of your model fields like changing
        order options,verbose_name, and a lot of other options.
        """
        model = Teacher
        fields = {
            'last_name': ['startswith'],
            'subject_taught__name': ['icontains']
        }
