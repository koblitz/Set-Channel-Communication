# -*- coding: utf-8 -*-
# Create your views here.
from datetime import date
from mysite.twitter.views import comment,retrieve

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

_date = date.today()

def twitter(request):
  
  comments = retrieve()
  return render_to_response('mysite/html/index.html', {'date':_date, 'comments':comments})
  
def post_twitter(request,text):
  if request.isAjax():
    comment(text,_date)
  #HttpResponseRedirect('/twitter/')  
  
