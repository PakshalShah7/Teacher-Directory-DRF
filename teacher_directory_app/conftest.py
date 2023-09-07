""" This file contains fixtures for the project. """

import pytest
from rest_framework.test import APIClient
from teacher_directory_app.factories import SubjectFactory, TeacherFactory
from teacher_directory_app.models import Subject, Teacher


@pytest.fixture
def create_subject() -> Subject:
    """
    This method should create fixture for subject.
    """
    factory = SubjectFactory.create()
    return factory


@pytest.fixture
def create_teacher() -> Teacher:
    """
    This method should create fixture for teacher.
    """
    factory = TeacherFactory.create()
    return factory


@pytest.fixture
def api_client():
    """
    This method should create fixture for client.
    """
    client = APIClient()
    return client
