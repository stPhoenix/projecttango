import requests
from django.db.models import ObjectDoesNotExist
import time
from news.models import Category
from journalist.utils.pcgamer import PCGamerReview


class Worker:
    MAX_ARTICLES = 20
    DEFAULT_CATEGORY_NAME = 'Interesting'

    def __init__(self):
        try:
            Category.objects.get(name=self.DEFAULT_CATEGORY_NAME)
        except ObjectDoesNotExist:
            print('Default category not found! Creating one')
            cat = Category.objects.create(name=self.DEFAULT_CATEGORY_NAME)
            cat.save()
            print('Default category created!')
        self.headers = requests.utils.default_headers()
        self.headers.update(
            {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                              ' (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
            }
        )

    def all(self):
        PCGamerReview(self.DEFAULT_CATEGORY_NAME, self.headers)
        print('Sleeping for 120 min')
        time.sleep(7200)
        self.all()

