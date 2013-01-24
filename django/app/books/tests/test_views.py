# coding: utf-8
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client
from factories import UserBookFactory


class UserBookListTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.userbook = UserBookFactory.create()

    def test_userbook_list(self):
        response = self.client.get(reverse('userbook_list', kwargs={'username': self.userbook.user.get_username()}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'userbook/userbook_list.html')
        self.assertEqual(response.context['user_book'].username, self.userbook.user.get_username())

    def test_userbook_list_error(self):
        self.userbook.user.username = 'xexa_gulima13'
        response = self.client.get(reverse('userbook_list', kwargs={'username': self.userbook.user.get_username()}))
        self.assertEqual(response.status_code, 404)
