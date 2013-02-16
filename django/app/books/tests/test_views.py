# coding: utf-8
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client
from accounts.tests.factories import UserFactory
from books.models import Book, UserBook


class BookCreationTestCase(TestCase):
    def setUp(self):
        super(BookCreationTestCase, self).setUp()
        self.client = Client()

        # creates a user and then log in
        self.user = UserFactory.create(username='testuser')
        self.user.set_password('testpass')
        self.user.save()

        self.client.login(username='testuser', password='testpass')

        self.data = {
            'title': u'Pro Django',
            'isbn': u'9781430210474',
        }

    def test_book_creation(self):
        response = self.client.post(reverse('books_creation'), self.data)
        self.assertRedirects(response, reverse('accounts_profile', kwargs={
            'username': self.user.username
        }))
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.all()[0].isbn, '9781430210474')
        self.assertEqual(UserBook.objects.count(), 1)
