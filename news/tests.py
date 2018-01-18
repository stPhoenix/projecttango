from django.test import TestCase
from django.template.loader import render_to_string
from django.utils import timezone
from account.models import Account
from news.models import Article, Category
from project.settings import TEMPLATE_PREFIX as TP
# Create your tests here.


class IndexTest(TestCase):
    def test_index_page(self):
        response = self.client.get('/')
        rendered_html = render_to_string('news/'+TP+'/index.html')
        self.assertEqual(200, response.status_code)
        self.assertHTMLEqual(response.content.decode(), rendered_html)
        self.assertTemplateUsed(response, 'news/'+TP+'/index.html')


class DetailTest(TestCase):
    def setUp(self):
        category = Category.objects.create(name='test category')
        category.save()
        self.article = Article.objects.create(title='Test article',
                                              pub_date=timezone.now(),
                                              article_text='Text for test article',
                                              category=category)
        self.article.save()

    def test_detail_page(self):
        response = self.client.get('/news/detail/%s/' % self.article.pk)
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'news/'+TP+'/detail.html')
        self.assertContains(response, 'Test article')
        self.assertContains(response, 'test category')
        self.assertContains(response, 'Text for test article')


class CommentingTest(TestCase):
    def setUp(self):
        user = Account.objects.create_user(
            username='jacob', email='jacob@mail.com', password='top_secret')
        category = Category.objects.create(name='test category')
        category.save()
        self.article = Article.objects.create(title='Test article',
                                              pub_date=timezone.now(),
                                              article_text='Text for test article',
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
        self.assertContains(request, "You didn&#39;t enter text.")


class AboutTest(TestCase):
    def test_about_page(self):
        response = self.client.get('/about/', follow=True)
        rendered_html = render_to_string('site/' + TP + '/about.html')
        self.assertEqual(200, response.status_code)
        self.assertHTMLEqual(response.content.decode(), rendered_html)
        self.assertTemplateUsed(response, 'site/' + TP + '/about.html')


class ContactUsTest(TestCase):
    def test_contact_us_page(self):
        response = self.client.get('/contact_us/', follow=True)
        rendered_html = render_to_string('site/' + TP + '/contact_us.html')
        self.assertEqual(200, response.status_code)
        self.assertHTMLEqual(response.content.decode(), rendered_html)
        self.assertTemplateUsed(response, 'site/' + TP + '/contact_us.html')


