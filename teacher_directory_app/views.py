""" This file contains views for subject, teacher and bulk. """

from http import HTTPStatus
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from teacher_directory_app.filters import TeacherFilter
from teacher_directory_app.models import Subject, Teacher
from teacher_directory_app.serializers import SubjectSerializer, TeacherSerializer, BulkSerializer


class SubjectView(ModelViewSet):
    """
    ModelViewSet for subject model provides the following actions.

    create: Create a new subject instance.
    retrieve: Return the given subject.
    update: Update the given subject instance.
    partial_update: Partially update the given subject instance.
    destroy: Deletes the given subject instance.
    list: Return a list of all existing subjects.
    """
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated]


class TeacherView(ModelViewSet):
    """
    ModelViewSet for teacher model provides the following actions.

    create: Create a new teacher instance.
    retrieve: Return the given teacher.
    update: Update the given teacher instance.
    partial_update: Partially update the given teacher instance.
    destroy: Deletes the given teacher instance.
    list: Return a list of all existing teachers.
    """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['last_name', 'subject_taught']
    filterset_class = TeacherFilter


class BulkView(CreateAPIView):
    """
    This view will create csv file having data of all teachers.
    """
    serializer_class = BulkSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """
        Returns response message when executed successfully.
        """
        super().create(request, *args, **kwargs)
        return Response("Data Uploaded Successfully", status=HTTPStatus.CREATED)
