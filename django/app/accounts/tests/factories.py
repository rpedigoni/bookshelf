# coding: utf-8
import factory
from accounts.models import User


class UserFactory(factory.Factory):
    FACTORY_FOR = User

    name = factory.Sequence(lambda n: 'Dr Rey {0}'.format(n))
    username = factory.Sequence(lambda n: 'drrey_{0}'.format(n))
    email = factory.Sequence(lambda n: 'drrey_{0}@hotmail.com'.format(n))
