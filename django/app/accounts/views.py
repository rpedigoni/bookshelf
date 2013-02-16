# coding: utf-8
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.views.generic import FormView, DetailView
from forms import LoginForm, UserCreationForm
from models import User


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'accounts/login.html'

    def get_success_url(self):
        return reverse('home')

    def form_valid(self, form):
        login(self.request, form.user_cache)
        return super(LoginView, self).form_valid(form)


class RegistrationView(FormView):
    form_class = UserCreationForm
    template_name = 'accounts/registration.html'

    def get_success_url(self):
        return reverse('home')

    def form_valid(self, form):
        form.save()
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
        login(self.request, user)
        return super(RegistrationView, self).form_valid(form)


class ProfileView(DetailView):
    model = User
    slug_url_kwarg = 'username'
    slug_field = 'username'
    template_name = 'accounts/profile.html'
