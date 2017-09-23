from django.test import TestCase, Client
from django.template.loader import render_to_string
from django.utils import timezone
from django.shortcuts import render
#from news.views import Index
from .views import Index
from .models import Article, Category
# Create your tests here.


class IndexTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        super(IndexTest, cls).setUpTestData()

    def test_index_page(self):
        response = self.client.get('/')
        rendered_html = render_to_string('news/index.html')
        self.assertEqual(200, response.status_code)
        self.assertHTMLEqual(response.content.decode(), rendered_html)
        self.assertTemplateUsed(response, 'news/index.html')


class DetailTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        super(DetailTest, cls).setUpTestData()
        category = Category.objects.create(name='test category')
        category.save()
        article = Article.objects.create(title='Test article',
                                         pub_date=timezone.now(),
                                         article_text='Text for test article',
                                         image='None.img',
                                         category=category)
        article.save()

    def test_detail_page(self):
        response = self.client.get('/news/1/')
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'news/detail.html')
        self.assertContains(response, 'Test article')
        self.assertContains(response, 'test category')
        self.assertContains(response, 'Text for test article')
        self.assertContains(response, 'None.img')