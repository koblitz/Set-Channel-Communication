from dajaxice.decorators import dajaxice_register
from apps.twitter.views import comment,retrieve
from django.template.loader import get_template
from django.template import Context
from django.utils import simplejson

@dajaxice_register
def post_twitter(request):
  text = request.GET.get('text', '')
    if text and len(text)<=70:
      comment(text,request.user.username,_date)
    comments = retrieve()
    refresh = get_template('index.html',Context({'date':_date, 'comments':comments, 'user':request.user.username}))
    return simplejson.dumps( {'response' : refresh.render()} )