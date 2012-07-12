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
    return render_to_response('mysite/html/index.html', {'date':_date, 'comments':comments, 'user':request.user.username})
  else:
    return render_to_response('mysite/html/login.html', {'date':_date})
  
def post_twitter(request):
  text = request.GET.get('text', '')
  if text and len(text)<=70:
      comment(text,request.user.username,_date)
  return HttpResponseRedirect('/twitter/')
  
def login(request):
  username = request.GET['login']
  passwd = request.GET['passwd']
  #cria um objeto user
  user = auth.authenticate(username=username, password=passwd)
  if user is not None and user.is_active:
    auth.login(request, user)
  return HttpResponseRedirect("/twitter/")
  
def logout(request):
  auth.logout(request)
  return HttpResponseRedirect("/twitter/")

 
    




  
