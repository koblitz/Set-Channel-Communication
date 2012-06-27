# -*- coding: utf-8 -*-
# Create your views here.
from models import Comments
from django.http import HttpResponseRedirect


def comment(text,date):
  #processamento
  c = Comments(date=today,author='',text=comment)
  c.save()

def retrieve():
  comments = Comments.objects.all()
  return comments.reverse()
    	
      		
  
  
  
  
  
  
