from journalist.utils.reviewbase import ReviewBase
from news.models import Article, Category, Tags, TITLE_MAX_LENGTH, TAG_MAX_LENGTH
from django.utils import timezone
import logging

logger = logging.getLogger(__name__)


class PCGamerReview(ReviewBase):
    def __init__(self, category, headers):
        super(PCGamerReview, self).__init__(category, headers)
        self.name = 'PCGamer'
        self.section = self.get_soup(self.WORK_URL).find(name='section', attrs={'data-next': 'latest'})
        self.start()

    def work(self):
        for ar in self.section.find_all(name='article', attrs={'class': 'search-result-news'}):
            if ar.parent['href'] != self.last_url and self.last_url_trigger is True:
                self.last_url_trigger = False
                self.memory.last_url = ar.parent['href']
            if ar.parent['href'] != self.last_url and self.articles <= self.MAX_ARTICLES:
                self.write_article(ar.parent['href'])
                self.articles += 1
                self.last_url = ar.parent['href']
            else:
                self.end_work = True
                break
        self.memory.save()
        next_page = self.section.find('span', attrs={'class': 'listings-next'}).a['href']
        section = self.get_soup(next_page).find(name='section', attrs={'data-next': 'latest'})

    def write_article(self, url):
        soup = self.get_soup(url).find('article')
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
                                         category=self.category)
        article.image_url = article_image_url if article_image_url is not None else article.image_url
        article.save()
        for tag in soup.find_all('div', attrs={'class': 'tag'}, limit=5):
            if len(tag.get_text()) <= TAG_MAX_LENGTH:
                t = Tags.objects.create(tag=tag.get_text(strip=True).replace(' ', ''), article=article)
                t.save()
        logger.info('Saved article: %s' % a_title)