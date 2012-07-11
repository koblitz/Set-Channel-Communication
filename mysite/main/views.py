# -*- coding: utf-8 -*-
# Create your views here.
from datetime import date
from mysite.twitter.views import comment,retrieve

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth

_date = date.today()

def twitter(request):
  if request.user.is_authenticated():
    comments = retrieve()
    return render_to_response('mysite/html/index.html', {'date':_date, 'comments':comments})
  else:
    return render_to_response('mysite/html/login.html', {'date':_date})
  
def post_twitter(request):
  text = request.GET.get('text', '')
  if text and len(text)<=70:
      comment(text,_date)
  return HttpResponseRedirect('/twitter/')
  
def login(request):
  user = request.POST.get('login', '')
  passwd = request.POST.get('passwd','')
  
