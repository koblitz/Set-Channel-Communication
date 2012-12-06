# -*- coding: utf-8 -*-
# Create your views here.
from time import gmtime, strftime
from mysite.twitter.models import Comments
from django.shortcuts import render_to_response

def twitter(request):
  
  date = strftime("%a, %d %b %Y %H:%M:%S", gmtime())
  
  comments = Comments.objects.all()
  
  comments.reverse()
  
  return render_to_response('mysite/html/index.html', {'date':date, 'list':comments})


  
  