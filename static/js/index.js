function send_comment() 
{     
      q = $('#comment_textarea').val();
	if (q.length > 70)
		alert('Seu Tweet precisa ter menos que 70 caracteres!');	
	else
		Dajaxice.call('apps.main.post_twitter', 'get', Dajax.process);
// 		Dajaxice.apps.main.post_twitter(Dajax.process);
	
};