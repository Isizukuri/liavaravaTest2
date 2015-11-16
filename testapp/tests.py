from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from .models import TextNote
# Create your tests here.


class TestHomePage(TestCase):

    def setUp(self):

        TextNote.objects.get_or_create(
            text="Test Note for Testing")

        TextNote.objects.get_or_create(
            text="Test Note for Testing 2")

        self.client = Client()

        self.url = reverse('home')

    def test_home_page(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)

        self.assertIn('Test Note for Testing', response.content)

        self.assertEqual(len(response.context['text_notes']), 2)
