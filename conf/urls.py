# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *

import settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('apps.main.views',
    (r'^twitter/$','twitter'),
    #(r'^twitter/post_twitter/$','post_twitter'),
    (r'^twitter/login/$','login'),
    (r'^twitter/logout/$','logout'),
    (r'^twitter/register/$','register'),
    (r'^twitter/register/create_user/$','create_user'),
)

urlpatterns += patterns('',
   (r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),
)

urlpatterns += staticfiles_urlpatterns()


