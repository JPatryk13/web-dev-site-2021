from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username=os.environ['SU_NAME']).exists():
            User.objects.create_superuser(os.environ['SU_NAME'], os.environ['SU_EMAIL'], os.environ['SU_PASSWORD'])
