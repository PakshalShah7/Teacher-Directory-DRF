""" This file contains serializers for subject and teacher model. """

import codecs
import csv
import os
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from teacher_directory_app.models import Subject, Teacher


class SubjectSerializer(serializers.ModelSerializer):
    """
    This is model serializer for subject model.
    """

    class Meta:
        """
        Model Meta is basically the inner class of your model class.
        Model Meta is basically used to change the behavior of your model fields like changing
        order options,verbose_name, and a lot of other options.
        """
        model = Subject
        fields = ['name']


class TeacherSerializer(serializers.ModelSerializer):
    """
    This is model serializer for teacher model.
    """
    teacher = serializers.HyperlinkedIdentityField(
        view_name='teacher_directory_app:teacher-detail')

    class Meta:
        """
        Model Meta is basically the inner class of your model class.
        Model Meta is basically used to change the behavior of your model fields like changing
        order options,verbose_name, and a lot of other options.
        """
        model = Teacher
        fields = ['first_name', 'last_name', 'profile_image', 'email_address', 'phone_number',
                  'room_number', 'subject_taught', 'teacher']

    def validate(self, attrs):
        """
        This method will validate that the subject taught by teacher should be less or equal to
        five or else raise validation error.
        """
        if len(attrs['subject_taught']) <= 5:
            return attrs
        raise ValidationError({'subject error': 'Maximum 5 subjects can be taught'})


class BulkSerializer(serializers.Serializer):
    """
    This is serializer for creating data from csv file in bulk.
    """
    file = serializers.FileField()

    def create(self, validated_data):
        """
        This method just creates the actual model instance using the validated_data.
        """
        file = validated_data['file']
        reader = csv.DictReader(codecs.iterdecode(file, "utf-8"), delimiter=",")
        data = list(reader)
        for row in data:
            if row["First Name"] != "":
                if not Teacher.objects.filter(email_address=row["Email Address"]).exists():
                    if os.path.exists('media/profile_images/' + row['Profile picture']):
                        profile_img = row['Profile picture']
                    else:
                        profile_img = 'profile_images/default_image.jpg'
                    teacher = Teacher.objects.create(first_name=row["First Name"],
                                                     last_name=row["Last Name"],
                                                     profile_image=profile_img,
                                                     email_address=row["Email Address"],
                                                     phone_number=row["Phone Number"],
                                                     room_number=row["Room Number"])
                    for subject in row['Subjects taught'].split(","):
                        new_subject, created = Subject.objects.get_or_create(
                            name=subject.strip().capitalize())
                        teacher.subject_taught.add(new_subject)
                else:
                    if os.path.exists('media/profile_images/' + row['Profile picture']):
                        profile_image = row['Profile picture']
                    else:
                        profile_image = 'profile_images/default_image.jpg'
                    existing_teacher = Teacher.objects.filter(email_address=row["Email Address"])
                    existing_teacher.update(
                        first_name=row["First Name"],
                        last_name=row["Last Name"],
                        profile_image=profile_image,
                        phone_number=row["Phone Number"],
                        room_number=row["Room Number"]
                    )
                    for subject in row['Subjects taught'].split(","):
                        new_subject, created = Subject.objects.get_or_create(
                            name=subject.strip().capitalize())
                        existing_teacher.first().subject_taught.add(new_subject)
        return validated_data
