""" This file contains urls for project. """

from django.urls import path, include
from rest_framework.routers import SimpleRouter
from teacher_directory_app.views import SubjectView, TeacherView, BulkView

app_name = 'teacher_directory_app'

router = SimpleRouter()
router.register('subject', SubjectView, basename='subject')
router.register('teacher', TeacherView, basename='teacher')

urlpatterns = [

    path('', include(router.urls)),
    path('create-bulk/', BulkView.as_view(), name='create-bulk')

]
