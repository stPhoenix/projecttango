from django.core.management.base import BaseCommand, CommandError
from django.core import management
from multiprocessing import Process
from journalist.worker import Worker


class Command(BaseCommand):
    help = 'This command run grabber and Django server in different process in parallel'

    def add_arguments(self, parser):
        parser.add_argument('addrport', nargs='?', help='Optional parameter for specifying address and port')

    def handle(self, *args, **options):
        worker = Process(target=Worker().all())
        worker.start()
        print('Hello from main code!')
        if options['addrport']:
            pass
        else:
            pass
        management.call_command('runserver', '--noreload', '--nothreading')
        # worker.terminate()