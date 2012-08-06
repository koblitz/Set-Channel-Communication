# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from django.conf import settings
from dajaxice.core import dajaxice_autodiscover


dajaxice_autodiscover()


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('mysite.main.views',
    (r'^twitter/$','twitter'),
    (r'^twitter/post_twitter/$','post_twitter'),
    (r'^twitter/login/$','login'),
    (r'^twitter/logout/$','logout'),
    (r'^twitter/register/$','register'),
    (r'^twitter/register/create_user/$','create_user'),
    (r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),
)
