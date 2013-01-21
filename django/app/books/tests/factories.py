# coding: utf-8
import factory
from accounts.tests.factories import UserFactory
from books.models import Book, UserBook


class BookFactory(factory.Factory):
    FACTORY_FOR = Book

    title = factory.Sequence(lambda n: 'Pro Django {0}'.format(n))
    isbn = u'9781430210474'


class UserBookFactory(factory.Factory):
    FACTORY_FOR = UserBook

    user = factory.SubFactory(UserFactory)
    book = factory.SubFactory(BookFactory)
