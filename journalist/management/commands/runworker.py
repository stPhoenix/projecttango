from django.core.management.base import BaseCommand, CommandError
from django.core import management
from multiprocessing import Process
from journalist.worker import Worker


class Command(BaseCommand):
    help = 'This command run Journalist'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        worker = Process(target=Worker().all())
        worker.start()