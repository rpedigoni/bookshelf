# coding: utf-8
from django import forms
from django.db import transaction
from models import Book


class BookCreationForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ('created_at',)

    def save(self, user, commit=True, *args, **kwargs):
        assert commit

        with transaction.commit_on_success():
            book = super(BookCreationForm, self).save(commit=True, *args, **kwargs)
            user.userbook_set.create(
                book=book,
            )

        return book
