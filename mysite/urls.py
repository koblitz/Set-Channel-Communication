# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *

from mysite.main.views import twitter,post_twitter,login,logout


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^twitter/$', twitter),
    (r'^twitter/post_twitter/$',post_twitter),
    (r'^twitter/login/$',login),
    (r'^twitter/logout/$',logout),
    #(r'^admin/', include('django.contrib.admin.urls')),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)
