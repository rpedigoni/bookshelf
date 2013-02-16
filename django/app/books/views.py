# coding: utf-8
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from util.mixins import ProtectedMixin
from forms import BookCreationForm


class BookCreationView(ProtectedMixin, CreateView):
    form_class = BookCreationForm
    template_name = 'books/book_creation.html'

    def form_valid(self, form):
        form.save(user=self.request.user)
        return HttpResponseRedirect(reverse('accounts_profile', kwargs={'username': self.request.user.username}))
