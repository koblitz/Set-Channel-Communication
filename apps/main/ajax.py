
from apps.twitter.views import comment,retrieve
from django.template.loader import render_to_string
from django.template import RequestContext

from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register

@dajaxice_register(method='GET', name='ajax.comment')
def post_twitter(request):
  
  text = request.GET['text']
  if text and len(text)<=70:
    comment(text,request.user.username,_date)
    comments = retrieve()
    refresh = render_to_string('index.html',RequestContext({'date':_date, 'comments':comments, 'user':request.user.username}))
    
    dajax = Dajax()
    dajax.assign('body','innerHTML',refresh)
    return dajax.json()