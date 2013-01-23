# coding: utf-8
from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns(
    '',
    url(r'^login/$', views.LoginView.as_view(), name='accounts_login'),
    url(r'^registration/$', views.RegistrationView.as_view(), name='accounts_registration'),
)
