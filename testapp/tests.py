# -*- coding: utf-8 -*-
from django.test import TestCase, SimpleTestCase, Client
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

        self.assertQuerysetEqual(TextNote.objects.all(),
                                 [repr(response.context['object_list'][0]),
                                  repr(response.context['object_list'][1])],
                                 ordered=False)


class TestWidgetPage(TestCase):

    def setUp(self):

        TextNote.objects.get_or_create(
            text="Test Note for Testing")

        TextNote.objects.get_or_create(
            text="Test Note for Testing 2")

        self.client = Client()

        self.url = reverse('widget')

    def test_widget_page(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'widget.html')

        # Checking if there is an element with help-text #
        # in rendered template to know, if it is properly rendered #
        self.assertInHTML(
            u'<h3 class="panel-title">Вставте це в код своєї \
             сторінки і матимете рендомну текстову нотатку \
             з нашого тестового сайту!</h3>', response.content)

        # Checking if link to widget is in rendered template.
        # It is impossible to do it in other way, because test client doesn`t
        # give host url
        self.assertIn('widget_return', response.content)


class TestWidgetReturn(TestCase, SimpleTestCase):

    def setUp(self):
        TextNote.objects.get_or_create(
            text="Test Note for Testing")

        TextNote.objects.get_or_create(
            text="Test Note for Testing 2")

        TextNote.objects.get_or_create(
            text="")

        TextNote.objects.get_or_create(
            text=u"Кирилична стрічка")

        TextNote.objects.get_or_create(
            text="abc" * 900)

        self.client = Client()

        self.url = reverse('widget_return')

    def test_widget_page(self):
        # creating notes - list of "text" attributes of all TextNote objects
        notes = [object.text for object in TextNote.objects.all()]

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)

        # Allocated random text note in response and checking if it is in notes
        self.assertIn(
            unicode(response.content.split('<div>')[1].split('</div>')[0]),
            notes)
