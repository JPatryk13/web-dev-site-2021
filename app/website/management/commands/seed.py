from django.core.management.base import BaseCommand
from faker import Faker
from ...models import Project


class Command(BaseCommand):
    help = 'Seeding (populating) tables.'

    def add_arguments(self, parser):
        parser.add_argument('--entries',
            default=5,
            type=int,
            help='The number of fake entries to create.')
        parser.add_argument('--table',
            default='Project',
            type=str,
            help='Model which table is to be populated (e.g. Project, Link)')

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

    proj = Project(
        title=faker.sentence(nb_words=5),
        prev_description=faker.text(max_nb_chars=200),
        description=faker.text(max_nb_chars=500),
        date_finished=faker.date()
    )
    proj.save()
    return proj

def create_link():
    return 'link'
