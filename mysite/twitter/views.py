# -*- coding: utf-8 -*-
# Create your views here.
from models import Comments
from django.http import HttpResponseRedirect


def comment(text,date):
  c = Comments(date=date,author='',text=text)
  c.save()

def retrieve():
  comments = Comments.objects.order_by("-id")
  return comments
    	
      		
  
  
  
  
  
  
