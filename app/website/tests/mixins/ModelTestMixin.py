from faker import Faker

from website.models import Project, Link, Image


class ModelTestMixin(object):
    """ Mixin with functions creating objects of models """
    faker = Faker('en_US')

    def create_project(self):
        # Create image for the project to be associated with
        img = self.create_image()
        # Return a project instance
        return Project.objects.create(
            title=self.faker.text(max_nb_chars=100),
            prev_description=self.faker.text(max_nb_chars=500),
            description=self.faker.text(max_nb_chars=2000),
            date_finished=self.faker.date(),
            img_id=img.id,
            public=True
        )

    def create_link(self):
        # Create test project for the link to be associated with
        proj = self.create_project()
        # Return a link instance
        return Link.objects.create(
            url_name=self.faker.text(max_nb_chars=200),
            url=self.faker.uri(),
            project=Project.objects.get(pk=proj.pk)
        )

    def create_image(self):
        # Return an image instance
        return Image.objects.create(
            url=self.faker.image_url(),
            img_name=self.faker.text(max_nb_chars=200)
        )
