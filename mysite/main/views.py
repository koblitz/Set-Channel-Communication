# -*- coding: utf-8 -*-
# Create your views here.
from datetime import date
from mysite.twitter.views import comment,retrieve
from django.shortcuts import render_to_response

def twitter(request):
  _date = date.today()
  if request.is_ajax():
    comment = request.GET.get('text','')	
    if comment and comment<70:
      comment(comment,data)
  comments = retrieve()
  return render_to_response('mysite/html/index.html', {'date':_date, 'comments':comments})

