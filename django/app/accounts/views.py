# coding: utf-8
from django.core.urlresolvers import reverse
from django.views.generic import FormView
from forms import UserCreationForm


class RegistrationView(FormView):
    form_class = UserCreationForm
    template_name = 'accounts/registration.html'

    def get_success_url(self):
        return reverse('home')

    def form_valid(self, form):
        form.save()
        return super(RegistrationView, self).form_valid(form)
