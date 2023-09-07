""" This file contains test cases for subject and teacher model. """

from http import HTTPStatus
import pytest
from teacher_directory_app.factories import SubjectFactory, TeacherFactory
from teacher_directory_app.models import Subject, Teacher
from user.models import User

pytestmark = pytest.mark.django_db


class TestSubject:
    """
    This class contains all test cases of subject model.
    """

    def test_subject_create(self, api_client):
        """
        This method should test that subject is created successfully.
        """
        data = {
            'name': 'Maths'
        }
        user = User.objects.create_user(username='pakshal', password='1234')
        api_client.force_authenticate(user)
        response = api_client.post('/subject/', data, format='json')
        assert response.status_code == HTTPStatus.CREATED
        assert Subject.objects.filter(name='Maths').exists()

    def test_subject_list(self, create_subject, api_client):
        """
        This method should test that it displays the list of subjects.
        """
        user = User.objects.create_user(username='pakshal', password='1234')
        api_client.force_authenticate(user)
        response = api_client.get('/subject/')
        assert response.status_code == HTTPStatus.OK
        assert len(response.data) == 1

    def test_subject_update(self, create_subject, api_client):
        """
        This method should test that it updates the subject name.
        """
        user = User.objects.create_user(username='pakshal', password='1234')
        api_client.force_authenticate(user)
        data = {
            'name': 'English'
        }
        response = api_client.put(f"/subject/{create_subject.pk}/", data=data, format='json')
        create_subject.refresh_from_db()
        assert response.status_code == HTTPStatus.OK
        assert create_subject.name == 'English'
        assert Subject.objects.filter(name='English').exists()

    def test_subject_delete(self, create_subject, api_client):
        """
        This method should test that it deletes the subject.
        """
        user = User.objects.create_user(username='pakshal', password='1234')
        api_client.force_authenticate(user)
        response = api_client.delete(f"/subject/{create_subject.pk}/")
        assert response.status_code == HTTPStatus.NO_CONTENT
        assert not Subject.objects.filter(id=create_subject.pk).exists()

    def test_subject_detail(self, create_subject, api_client):
        """
        This method should test that it shows detail of a subject.
        """
        user = User.objects.create_user(username='pakshal', password='1234')
        api_client.force_authenticate(user)
        response = api_client.get(f"/subject/{create_subject.pk}/")
        assert response.status_code == HTTPStatus.OK
        assert response.data['name'] == create_subject.name


class TestTeacher:
    """
    This class contains all test cases of teacher model.
    """

    def test_teacher_create(self, api_client):
        """
        This method should test that teacher is created successfully.
        """
        subject = SubjectFactory.create()
        teacher = TeacherFactory.build(subject_taught=[subject])
        data = {
            'first_name': 'Pakshal',
            'last_name': 'Shah',
            'profile_image': teacher.profile_image,
            'email_address': 'teacher54@example.com',
            'phone_number': 1234567890,
            'room_number': '1A',
            'subject_taught': [subject.id]
        }
        response = api_client.post('/teacher/', data)
        assert response.status_code == HTTPStatus.CREATED
        assert Teacher.objects.filter(email_address='teacher54@example.com').exists()

    def test_teacher_list(self, create_teacher, api_client):
        """
        This method should test that it displays the list of teachers.
        """
        response = api_client.get('/teacher/')
        assert response.status_code == HTTPStatus.OK
        assert len(response.data) == 1

    def test_teacher_update(self, create_teacher, api_client):
        """
        This method should test that it updates the teacher data.
        """
        subject = SubjectFactory.create()
        teacher = TeacherFactory.build(subject_taught=[subject])
        data = {
            'first_name': 'John',
            'last_name': 'Wick',
            'profile_image': teacher.profile_image,
            'email_address': 'teacher54@example.com',
            'phone_number': 1234567890,
            'room_number': '1A',
            'subject_taught': [subject.id]
        }
        response = api_client.put(f"/teacher/{create_teacher.pk}/", data=data)
        create_teacher.refresh_from_db()
        assert response.status_code == HTTPStatus.OK
        assert create_teacher.first_name == 'John'
        assert Teacher.objects.filter(first_name='John').exists()

    def test_teacher_delete(self, create_teacher, api_client):
        """
        This method should test that it deletes the teacher.
        """
        response = api_client.delete(f"/teacher/{create_teacher.pk}/")
        assert response.status_code == HTTPStatus.NO_CONTENT
        assert not Teacher.objects.filter(id=create_teacher.pk).exists()

    def test_teacher_detail(self, create_teacher, api_client):
        """
        This method should test that it shows detail of a teacher.
        """
        response = api_client.get(f"/teacher/{create_teacher.pk}/")
        assert response.status_code == HTTPStatus.OK
        assert response.data['first_name'] == create_teacher.first_name
