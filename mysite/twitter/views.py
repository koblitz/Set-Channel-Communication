# -*- coding: utf-8 -*-
# Create your views here.
from models import Comments
from django.http import HttpResponseRedirect

def comment(request):
  #processamento
  comment = request.GET.get('text','')
  c = Comments(date='',author='',text=comment)
  return HttpResponseRedirect('/twitter/')
  
