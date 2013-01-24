# coding: utf-8
from django.http import Http404
from django.views.generic import ListView
from models import UserBook
from accounts.models import User


class UserBookListView(ListView):
    template_name = 'userbook/userbook_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        try:
            user = User.objects.get(username=self.kwargs.get('username'))
            queryset = UserBook.objects.filter(user=user)
        except:
            return None

        return queryset

    def get_context_data(self, **kwargs):
        context = super(UserBookListView, self).get_context_data(**kwargs)
        try:
            context['user_book'] = User.objects.get(username=self.kwargs.get('username'))
        except:
            raise Http404
        return context
