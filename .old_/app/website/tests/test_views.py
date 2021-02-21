from django.test import TestCase
from django.contrib.auth import get_user_model
from .mixins.ViewTestMixin import ViewTestMixin
from .mixins.ModelTestMixin import ModelTestMixin
import random
from faker import Faker
import os

from website import views


class IndexTest(TestCase, ViewTestMixin):
    view_class = views.Index

    def test_get_request(self):
        self.is_callable()

    def test_post_request(self):
        self.is_callable(
            post=True,
            to='contact-success',
            data={
                'name': 'John Smith',
                'email': 'jsmith@gmail.com',
                'message': 'Hi! How things are going?'
            }
        )


class ProjectDetailViewTest(TestCase, ViewTestMixin, ModelTestMixin):
    view_class = views.ProjectDetailView

    def setUp(self):
        self.proj = self.create_project()

    def test_get_request(self):
        self.is_callable(kwargs={'pk': self.proj.pk})


class HireMeTest(TestCase, ViewTestMixin):
    view_class = views.HireMe

    def setUp(self):
        self.faker = Faker('en_US')

    def test_get_request(self):
        self.is_callable()

    def test_post_request(self):
        self.is_callable(
            post=True,
            to='hire-me-success',
            data={
                'name': 'John Smith',
                'email': 'jsmith@gmail.com',
                'project_type': random.choice(['d', 'b', 'f', 's']),
                'project_status': random.choice(['e', 'n']),
                'description': self.faker.text(max_nb_chars=500)
            }
        )


class UploadTest(TestCase, ViewTestMixin):
    view_class = views.Upload

    def setUp(self):
        # Create user with superuser permissions
        User = get_user_model()
        # self.s_user = User.objects.get(username=os.environ['SU_NAME'])
        # self.s_user.is_staff = True
        # self.s_user.is_admin = True
        # self.s_user.is_superuser = True
        # self.s_user.save()
        self.s_user = User.objects.create_superuser(os.environ['SU_NAME'], os.environ['SU_EMAIL'], os.environ['SU_PASSWORD'])
        self.faker = Faker('en_US')

    def test_anonymous_user(self):
        self.is_forbidden()

    def test_get_request(self):
        self.is_callable(user=self.s_user)

    def test_post_request(self):
        self.is_callable(
            user=self.s_user,
            post=True,
            to='upload',
            data={
                'img_name': self.faker.text(max_nb_chars=100)
            },
            kwargs={
                'image_file': self.faker.image_url()
            }
        )
