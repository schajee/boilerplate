from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = 'Generates initial data for testing'

    def handle(self, *args, **options):
        user = User.objects.create_user(
            username='admin',
            email='info@example.com',
            password='admin',
            first_name='System',
            last_name='Administrator',
            is_superuser=True,
            is_staff=True,
        )
        user.save()
