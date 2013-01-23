# coding: utf-8
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django.utils.translation import ugettext as _
from models import User


class LoginForm(forms.Form):
    error_messages = {
        'bad_credentials': _('User or password incorrect')
    }

    username = forms.CharField(label=_('username'), max_length=20)
    password = forms.CharField(label=_('password'), max_length=20)

    def clean(self, *args, **kwargs):
        cleaned_data = super(LoginForm, self).clean(*args, **kwargs)
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError(self.error_messages['bad_credentials'])
        self.user_cache = user
        return cleaned_data


class UserCreationForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = ('name', 'email', 'username')

    def clean_username(self):
        username = self.cleaned_data['username']

        try:
            self._meta.model.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])
