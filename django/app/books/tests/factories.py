# coding: utf-8
import factory
from accounts.tests.factories import UserFactory
from books.models import Book, UserBook


class BookFactory(factory.Factory):
    FACTORY_FOR = Book

    title = factory.Sequence(lambda n: 'Pro Django {0}'.format(n))
    isbn_10 = u'1430210478'
    isbn_13 = u'978-1430210474'


class UserBookFactory(factory.Factory):
    FACTORY_FOR = UserBook

    user = factory.SubFactory(UserFactory)
    book = factory.SubFactory(BookFactory)
