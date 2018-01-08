from django.core.management.base import BaseCommand, CommandError
from journalist.worker import Worker


class Command(BaseCommand):
    help = 'This command run Journalist'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        Worker().all()