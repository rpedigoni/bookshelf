from django.test import TestCase


class BooksAppTestCase(TestCase):
    def test_test(self):
        self.assertEqual(1 + 1, 2)
