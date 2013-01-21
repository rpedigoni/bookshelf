# coding: utf-8
from django import forms
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from models import User


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
