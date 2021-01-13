from django.core.management.base import BaseCommand
from faker import Faker
from ...models import Project, Link, Image
import random


class Command(BaseCommand):
    help = 'Seeding (populating) tables.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--entries',
            default=5,
            type=int,
            help='The number of fake entries to create.'
        )
        parser.add_argument(
            '--table',
            default='Project',
            type=str,
            help='Model which table is to be populated (e.g. Project, Link)'
        )

    def handle(self, *args, **options):
        if options['table'] == 'Project':
            print('Seeding ' + str(options['entries']) + ' objects to the Project table...')
            for _ in range(options['entries']):
                create_project()
        else:
            print('Seeding ' + str(options['entries']) + ' objects to the Link table...')
            for _ in range(options['entries']):
                create_link()
        print('Done')


def create_project():
    faker = Faker('en_US')

    img = Image(
        url=faker.image_url(),
        img_name=faker.text(max_nb_chars=100)
    )
    img.save()
    proj = Project(
        title=faker.text(max_nb_chars=100),
        prev_description=faker.text(max_nb_chars=500),
        description=faker.text(max_nb_chars=2000),
        date_finished=faker.date(),
        img_id=img.id
    )
    proj.save()
    return proj


def create_link():
    faker = Faker('en_US')

    project_ids = Project.objects.all().values_list('id', flat=True)
    # is empty when there in no projects in the list

    lnk = Link(
        url_name=faker.text(max_nb_chars=200),
        url=faker.uri(),
        project=Project.objects.get(pk=random.choice(project_ids))
    )
    lnk.save()
    return lnk
