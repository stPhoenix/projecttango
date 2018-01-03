import os
import sys
import requests
from tempfile import NamedTemporaryFile
import django
from django.core.files import File
from django.utils import timezone
from bs4 import BeautifulSoup as bs4
from django.db.models import ObjectDoesNotExist
import time


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


    def test_db(self):
        print('Testing db')
        Article.objects.create(title="Test title",
                               pub_date=timezone.now(),
                               article_text="Text "*20,
                               image="avatar.jpg",
                               category=Category.objects.create(name="Test category"))
        #print(Article.objects.all())

    def pcgamer_com_review(self):
        print('Starting PCGamer review')
        WORK_URL = 'http://www.pcgamer.com/news/'
        articles = 0
        last_url = ''
        category = Category.objects.get(name=self.DEFAULT_CATEGORY_NAME)
        end_work = False
        memory = None
        last_url_trigger = True

        # def download_image(url, field):
        #     try:
        #         r = requests.get(url)
        #         if r.status_code == requests.codes.ok:
        #             img_temp = NamedTemporaryFile(delete=True)
        #             img_temp.write(r.content)
        #             img_temp.flush()
        #
        #             img_filename = url.split('/')[-1]
        #
        #             field.save(img_filename, File(img_temp), save=True)
        #     except requests.exceptions.MissingSchema:
        #         print('Can\'t download image. Maybe url wrong.')

        def write_article(url):
            soup = get_soup(url).find('article')
            article_body = soup.find('div', attrs={'itemprop': 'articleBody'})
            article_text = ''
            article_image_url = None
            a_title = soup.find('h1').get_text()
            a_title = a_title[:TITLE_MAX_LENGTH - 3] + '...' if len(a_title) > TITLE_MAX_LENGTH else a_title
            for p in article_body.find_all('p'):
                if p.get('class') == ['bordeaux-image-check']:
                    article_image_url = p.img['data-original-mos']
                else:
                    article_text += str(p)
            article_text += '<p> Source <a href="%s">PCGamer</a></p>' % url
            article = Article.objects.create(title=a_title,
                                             pub_date=timezone.now(),
                                             article_text=article_text,
                                             category=category)
            article.image_url = article_image_url if article_image_url is not None else article.image_url
            article.save()
            for tag in soup.find_all('div', attrs={'class': 'tag'}, limit=5):
                if len(tag.get_text()) <= TAG_MAX_LENGTH:
                    t = Tags.objects.create(tag=tag.get_text(strip=True).replace(' ', ''), article=article)
                    t.save()
            print('Saved article: %s' % a_title)
            #download_image(article_image_url, article.image)

        def get_soup(url):
            req = requests.get(url, headers=self.headers)
            if req.status_code == requests.codes.ok:
                return bs4(req.text, 'html.parser')
            else:
                raise requests.exceptions.HTTPError
        try:
            memory = WorkerMemory.objects.get(name='PCGamer')
            last_url = memory.last_url
        except ObjectDoesNotExist:
            print("Object does not exist! Creating one...")
            memory = WorkerMemory.objects.create(name='PCGamer', last_url='')
            memory.save()
            print('Object created!')
        section = get_soup(WORK_URL).find(name='section', attrs={'data-next': 'latest'})
        while end_work is False:
            for ar in section.find_all(name='article', attrs={'class': 'search-result-news'}):
                if ar.parent['href'] != last_url and last_url_trigger is True:
                    last_url_trigger = False
                    memory.last_url = ar.parent['href']
                if ar.parent['href'] != last_url and articles <= self.MAX_ARTICLES:
                    write_article(ar.parent['href'])
                    articles += 1
                    last_url = ar.parent['href']
                else:
                    end_work = True
                    break
            memory.save()
            next_page = section.find('span', attrs={'class': 'listings-next'}).a['href']
            section = get_soup(next_page).find(name='section', attrs={'data-next': 'latest'})
        print('Last url: %s' % memory.last_url)
        print('PCGamer review finished!')

    def all(self):
        self.pcgamer_com_review()
        print('Sleeping for 60 min')
        time.sleep(3600)


if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'project.settings')
    sys.path.append(BASE_DIR)
    django.setup()
    from news.models import Article, Category
    Worker().test_db()
else:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'project.settings')
    sys.path.append(BASE_DIR)
    django.setup()
    from news.models import Article, Category, Tags, TITLE_MAX_LENGTH, TAG_MAX_LENGTH
    from .models import WorkerMemory

