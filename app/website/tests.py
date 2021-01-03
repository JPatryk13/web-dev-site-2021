from django.test import TestCase
from faker import Faker
from .models import Project

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

    def test_project_creation(self):
        # In principle: create an instance of Project class
        proj = self.create_project()
        # Test if the 'proj' is an instance of the 'Project' class
        self.assertTrue(isinstance(proj, Project))
        # Test if the __str__ function return proj.title
        self.assertEqual(proj.__str__(), proj.title)
