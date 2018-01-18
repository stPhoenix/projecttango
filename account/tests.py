from django.test import TestCase
from django.template.loader import render_to_string
from account.models import Account
from project.settings import TEMPLATE_PREFIX as TP

# Create your tests here.


class LoginTest(TestCase):
    def test_login_page(self):
        self.maxDiff = None
        response = self.client.get('/login/')
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'account/'+TP+'/login.html')


class SignUpTest(TestCase):
    def test_signup_page(self):
        response = self.client.get('/account/sign_up/')
        rendered_html = render_to_string('account/'+TP+'/sign_up.html')
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'account/'+TP+'/sign_up.html')


class LogOutTest(TestCase):
    def setUp(self):
        user = Account.objects.create_user(
            username='jacob', email='jacob@mail.com', password='top_secret')
        self.client.login(username='jacob', password='top_secret')

    def test_logout_page(self):
        response = self.client.get('/logout/', follow=True)
        rendered_html = render_to_string('news/'+TP+'/index.html')
        self.assertEqual(200, response.status_code)
        self.assertHTMLEqual(response.content.decode(), rendered_html)
        self.assertTemplateUsed(response, 'news/'+TP+'/index.html')