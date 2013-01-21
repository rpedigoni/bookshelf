# coding: utf-8
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext as _


class UserManager(BaseUserManager):
    pass


class User(AbstractBaseUser):
    REQUIRED_FIELDS = ['name', 'email']
    USERNAME_FIELD = 'username'

    name = models.CharField(_('name'), max_length=128)
    username = models.CharField(_('username'), max_length=20, unique=True)
    email = models.EmailField(_('e-mail'), unique=True)

    objects = UserManager()

    class Meta:
        verbose_name, verbose_name_plural = _('user'), _('users')

    def __unicode__(self):
        return self.name
