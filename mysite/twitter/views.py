# -*- coding: utf-8 -*-
# Create your views here.
from models import Comments
from django.http import HttpResponseRedirect
from datetime import date

def comment(request):
  #processamento
  comment = request.GET.get('text','')
  if comment:
    today = date.today()
  if len(comment)>70:
    return HttpResponseRedirect('/twitter/')
  c = Comments(date=today,author='',text=comment)
  c.save()
  return HttpResponseRedirect('/twitter/')
  
