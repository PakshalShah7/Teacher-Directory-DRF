""" This file contains signup and login views. """

from django.contrib.auth import login
from knox.views import LoginView as KnoxLoginView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from user.serializers import UserSerializer


class SignupView(CreateAPIView):
    """
    This class will create new user instance.
    """
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class LoginView(KnoxLoginView):
    """
    This class will authenticate and authorized the requested user if user input correct
    credentials.
    """
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        """
        This method will log in the user with Token.
        """
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)
