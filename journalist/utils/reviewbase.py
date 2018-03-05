import logging
import requests
from journalist.models import WorkerMemory
from bs4 import BeautifulSoup as bs4
from django.db.models import ObjectDoesNotExist
from news.models import Category

logger = logging.getLogger(__name__)


class ReviewBase:
    def __init__(self, category, headers):
        self.WORK_URL = None
        self.articles = 0
        self.last_url = ''
        self.category = Category.objects.get(name=category)
        self.end_work = False
        self.memory = None
        self.last_url_trigger = True
        self.headers = headers
        self.name = 'ReviewName'
        self.section = None
        try:
            self.memory = WorkerMemory.objects.get(name=self.name)
            self.last_url = self.memory.last_url
        except ObjectDoesNotExist:
            logger.info("Object does not exist! Creating one...")
            self.memory = WorkerMemory.objects.create(name=self.name, last_url='')
            self.memory.save()
            logger.info('Object created!')

    def start(self):
        while self.end_work is False:
            self.work()
        logger.info('Last url: %s' % self.memory.last_url)
        logger.info('%s review finished!' % self.name)

    def get_soup(self, url):
        req = requests.get(url, headers=self.headers)
        if req.status_code == requests.codes.ok:
            return bs4(req.text, 'html.parser')
        else:
            raise requests.exceptions.HTTPError

