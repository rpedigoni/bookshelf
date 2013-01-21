# coding: utf-8
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    '',
    # url(r'^admin/', include(admin.site.urls)),
    url(
        r'^$',
        TemplateView.as_view(
            template_name='home.html',
        ),
        name='home',
    ),
    url(r'^accounts/', include('accounts.urls')),
)
