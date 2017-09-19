from django.test import TestCase, Client
from django.template.loader import render_to_string
#from news.views import Index
from .views import Index
# Create your tests here.


class IndexTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def test_index_page(self):
        result = self.client.get('/')
        rendered_html = render_to_string('news/index.html')
        self.assertEqual(200, result.status_code)
        self.assertAlmostEqual(result.body, rendered_html)