# coding: utf-8
from django.test import TestCase
from factories import BookFactory, UserBookFactory


class BookTestCase(TestCase):
    def test_unicode(self):
        book = BookFactory.create()
        self.assertEqual(unicode(book), book.title)


class UserBookTestCase(TestCase):
    def test_unicode_with_id(self):
        user_book = UserBookFactory.create()
        self.assertEqual(unicode(user_book), u'Book {0}'.format(user_book.id))

    def test_unicode_without_id(self):
        user_book = UserBookFactory.build()
        self.assertEqual(unicode(user_book), u'Unregistered book')
