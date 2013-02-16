# coding: utf-8
from django.conf.urls import patterns, url
import views

urlpatterns = patterns(
    '',
    url(
        r'^add/$',
        views.BookCreationView.as_view(),
        name='books_creation',
    ),
)
