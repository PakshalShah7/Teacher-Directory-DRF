""" This file contains urls of project. """

from django.urls import path
from knox.views import LogoutView, LogoutAllView
from user.views import SignupView, LoginView

app_name = 'user'

urlpatterns = [

    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='knox_login'),
    path('logout/', LogoutView.as_view(), name='knox_logout'),
    path('logout-all/', LogoutAllView.as_view(), name='knox_logoutall'),

]
