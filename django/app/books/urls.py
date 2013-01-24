# coding: utf-8
from django.conf.urls import patterns, url
import views

urlpatterns = patterns(
    '',
    url(
        r'^userbook/(?P<username>[a-zA-Z0-9_]+)/$',
        views.UserBookListView.as_view(),
        name='userbook_list'
    ),
)
