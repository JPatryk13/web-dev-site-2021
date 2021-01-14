from django.test import TestCase
from faker import Faker
from website.models import Project, Link, Image
from .mixins.ModelTestMixin import ModelTestMixin

# Models test
class ProjectTest(TestCase, ModelTestMixin):

    def setUp(self):
        # Create an instance of Project class
        self.proj = self.create_project()

    def test_str(self):
        # Test if the __str__ function returns proj.title
        self.assertEqual(self.proj.__str__(), self.proj.title)

    def test_get_absolute_url(self):
        # Test if get_absolute_url function returns proj.id
        self.assertEqual(self.proj.get_absolute_url(), '/project/' + str(self.proj.pk))


class LinkTest(TestCase, ModelTestMixin):

    def setUp(self):
        # Create an instance of Link class
        self.link = self.create_link()

    def test_str(self):
        # Test if the __str__ function returns link.url_name
        self.assertEqual(self.link.__str__(), self.link.url_name)
