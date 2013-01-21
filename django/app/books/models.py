# coding: utf-8
from django.db import models
from django.utils.translation import ugettext as _
from django.utils.timezone import now
from accounts.models import User


class Book(models.Model):
    title = models.CharField(_('title'), max_length=254)
    #TODO: validate isbn
    # ISBN10 IDs are also valid on ISBN13, just prepend 978
    isbn = models.CharField(_('ISBN 13'), max_length=13, blank=True, null=True)
    created_at = models.DateTimeField(_('created at'), default=now)

    class Meta:
        verbose_name, verbose_name_plural = _('book'), _('books')

    def __unicode__(self):
        return self.title


class UserBook(models.Model):
    book = models.ForeignKey(Book, verbose_name=_('book'))
    user = models.ForeignKey(User, verbose_name=_('user'))
    created_at = models.DateTimeField(_('created at'), default=now)

    class Meta:
        verbose_name, verbose_name = _('user book'), _('user books')

    def __unicode__(self):
        if self.id:
            return _('Book {0}').format(self.id)
        return _('Unregistered book')
