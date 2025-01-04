# In your project/management/commands directory
from django.core.management.base import BaseCommand
from django.core.management import call_command
class Command(BaseCommand):
    help = 'Run the User Service'

    def handle(self, *args, **kwargs):
        # Specify the port for the User Service
        call_command('runserver', '127.0.0.1:8005')

# Similar commands for other microservices