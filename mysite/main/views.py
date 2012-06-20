# -*- coding: utf-8 -*-
# Create your views here.
from time import gmtime, strftime
from django.shortcuts import render_to_response

def twitter(request):
  date = strftime("%a, %d %b %Y %H:%M:%S", gmtime())
  return render_to_response('mysite/src/html/template.html', {'date':date})

