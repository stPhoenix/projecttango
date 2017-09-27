from django.test import TestCase, Client
from django.template.loader import render_to_string
from django.utils import timezone
from account.models import Account
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
    def setUp(self):
        category = Category.objects.create(name='test category')
        category.save()
        self.article = Article.objects.create(title='Test article',
                                              pub_date=timezone.now(),
                                              article_text='Text for test article',
                                              image='None.img',
                                              category=category)
        self.article.save()

    def test_detail_page(self):
        response = self.client.get('/news/%s/' % self.article.pk)
        print(response.content.decode())
        print('Article pk: %s' % self.article.pk)
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'news/detail.html')
        self.assertContains(response, 'Test article')
        self.assertContains(response, 'test category')
        self.assertContains(response, 'Text for test article')
        self.assertContains(response, 'None.img')


class CommentingTest(TestCase):
    def setUp(self):
        user = Account.objects.create_user(
            username='jacob', email='jacob@mail.com', password='top_secret')
        category = Category.objects.create(name='test category')
        category.save()
        self.article = Article.objects.create(title='Test article',
                                              pub_date=timezone.now(),
                                              article_text='Text for test article',
                                              image='None.img',
                                              category=category)
        self.article.save()
        self.client.login(username='jacob', password='top_secret')

    def test_commenting(self):
        request = self.client.post('/news/%s/add_comment' % self.article.pk, {'comment_text': 'test comment'}, follow=True)
        self.assertEqual(request.status_code, 200)
        self.assertContains(request, 'test comment')

    def test_void_text_comment(self):
        request = self.client.post('/news/%s/add_comment' % self.article.pk, {'comment_text': ''}, follow=True)
        self.assertEqual(request.status_code, 200)
        self.assertContains(request, "You didn't enter text.")



