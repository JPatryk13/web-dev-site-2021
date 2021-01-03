from django.test import TestCase
from faker import Faker
from ..models import Project, Link
import random

# Models test
class ProjectTest(TestCase):

    faker = Faker('en_US')

    def create_project(self):
    # Return a project instance
        return Project.objects.create(
            title=self.faker.text(max_nb_chars=100),
            prev_description=self.faker.text(max_nb_chars=500),
            description=self.faker.text(max_nb_chars=2000),
            date_finished=self.faker.date(),
            img=self.faker.image_url(),
            public=True
        )

    def test_str(self):
        # In principle: create an instance of Project class
        proj = self.create_project()
        # Test if the 'proj' is an instance of the 'Project' class
        self.assertTrue(isinstance(proj, Project))
        # Test if the __str__ function returns proj.title
        self.assertEqual(proj.__str__(), proj.title)

    def test_get_absolute_url(self):
        proj = self.create_project()
        self.assertTrue(isinstance(proj, Project))
        # Test if get_absolute_url function returns proj.id
        self.assertEqual(proj.get_absolute_url(), '/project/' + str(proj.id))


class LinkTest(TestCase):

    faker = Faker('en_US')

    def create_link(self):
        # Create test project for the link to be associated with
        proj = Project.objects.create(
            title=self.faker.text(max_nb_chars=100),
            prev_description=self.faker.text(max_nb_chars=500),
            description=self.faker.text(max_nb_chars=2000),
            date_finished=self.faker.date(),
            img=self.faker.image_url(),
            public=True
        )
        # Return a link instance
        return Link.objects.create(
            url_name=self.faker.text(max_nb_chars=200),
            url=self.faker.uri(),
            project=Project.objects.get(pk=proj.id)
        )

    def test_str(self):
        # In principle: create an instance of Link class
        link = self.create_link()
        # Test if the 'link' is an instance of the 'Link' class
        self.assertTrue(isinstance(link, Link))
        # Test if the __str__ function returns link.url_name
        self.assertEqual(link.__str__(), link.url_name)
