# -*- coding: utf-8 -*-
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from datetime import date
from apps.twitter.views import retrieve

from django.shortcuts import render_to_response
from django.template import Context
from django.http import HttpResponseRedirect
from django.contrib import auth

from django.contrib.auth.models import User

_date = date.today()

def twitter(request):
  if request.user.is_authenticated():
    comments = retrieve()
    return render_to_response('index.html', {'date':_date, 'comments':comments, 'user':request.user.username})
  else:
    return render_to_response('login.html', {'date':_date})

@csrf_exempt
def login(request):
  username = request.POST['login']
  passwd = request.POST['passwd']
  #cria um objeto user
  user = auth.authenticate(username=username, password=passwd)
  if user is not None and user.is_active:
    auth.login(request, user)
  return HttpResponseRedirect("/twitter/")
  
def logout(request):
  auth.logout(request)
  return HttpResponseRedirect("/twitter/")

@csrf_exempt
def create_user(request):
  username = request.POST['new_login']
  passwd = request.POST['new_passwd']
  user = User.objects.create_user(username=username,password=passwd)
  return HttpResponseRedirect('/twitter/')
  
def register(request):
  return render_to_response('register.html')

  
  

 
    




  
