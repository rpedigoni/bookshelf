# coding: utf-8
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client
from factories import UserFactory
from accounts.forms import LoginForm
from accounts.models import User


class UserLoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login_ok(self):
        user = UserFactory.create(username='test')
        user.set_password('test')
        user.save()

        response = self.client.post(reverse('accounts_login'), {
            'username': 'test',
            'password': 'test',
        })
        self.assertRedirects(response, '/')

    def test_login_error(self):
        user = UserFactory.create(username='test')
        user.set_password('badtest')
        user.save()

        response = self.client.post(reverse('accounts_login'), {
            'username': 'test',
            'password': 'test',
        })
        self.assertContains(response, LoginForm.error_messages['bad_credentials'])


class UserCreationTestCase(TestCase):
    def setUp(self):
        super(UserCreationTestCase, self).setUp()
        self.client = Client()
        self.data = {
            'name': u'Renato Pedigoni',
            'email': u'rpedigoni@xpto.com',
            'username': u'rpedigoni',
            'password1': u'123example',
            'password2': u'123example',
        }

    def test_user_registration(self):
        response = self.client.post(reverse('accounts_registration'), self.data)
        self.assertRedirects(response, '/')
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.all()[0].username, 'rpedigoni')

    def test_user_registration_form_error(self):
        self.data.update({'password2': 'bad'})
        response = self.client.post(reverse('accounts_registration'), self.data)
        self.assertContains(response, u'Erro ao processar formulário')

    def test_user_check_duplicated_username(self):
        # create a user
        UserFactory.create(username='duplicate')

        # try to create another user with the same username
        self.data.update({'username': 'duplicate'})
        response = self.client.post(reverse('accounts_registration'), self.data)
        self.assertContains(response, u'Erro ao processar formulário')
