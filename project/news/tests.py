from django.test import TestCase, Client
from django.template.loader import render_to_string
from django.shortcuts import render
#from news.views import Index
from .views import Index
# Create your tests here.


class IndexTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def test_index_page(self):
        response = self.client.get('/')
        rendered_html = render_to_string('news/index.html')
        self.assertEqual(200, response.status_code)
        self.assertHTMLEqual(response.content.decode(), rendered_html)
