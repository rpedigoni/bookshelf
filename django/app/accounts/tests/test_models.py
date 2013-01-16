# coding: utf-8
from django.test import TestCase
from factories import UserFactory


class UserTestCase(TestCase):
    def test_unicode(self):
        user = UserFactory.create()
        self.assertEqual(unicode(user), user.name)
