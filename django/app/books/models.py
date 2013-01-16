# coding: utf-8
from django.db import models
from django.utils.translation import ugettext as _
from accounts.models import User


class Book(models.Model):
    title = models.CharField(_('title'), max_length=254)
    #TODO: validate isbn
    isbn_10 = models.CharField(_('ISBN 10'), max_length=10, blank=True, null=True)
    isbn_13 = models.CharField(_('ISBN 13'), max_length=14, blank=True, null=True)

    class Meta:
        verbose_name, verbose_name_plural = _('book'), _('books')

    def __unicode__(self):
        return self.title


class UserBook(models.Model):
    book = models.ForeignKey(Book, verbose_name=_('book'))
    user = models.ForeignKey(User, verbose_name=_('user'))

    class Meta:
        verbose_name, verbose_name = _('user book'), _('user books')

    def __unicode__(self):
        if self.id:
            return _('Book {0}').format(self.id)
        return _('Unregistered book')
