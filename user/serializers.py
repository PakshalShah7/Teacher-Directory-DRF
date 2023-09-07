""" This file contains user serializer which will use in project. """

from rest_framework import serializers
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    This is model serializer for user model.
    """

    class Meta:
        """
        Model Meta is basically the inner class of your model class.
        Model Meta is basically used to change the behavior of your model fields like changing
        order options,verbose_name, and a lot of other options.
        """
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        This method just creates the actual model instance using the validated_data.
        """
        user = User.objects.create_user(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
