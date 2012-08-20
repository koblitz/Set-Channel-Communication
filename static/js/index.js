 
 $(document).ready(function(){
	$('#comment_submit').click(function() {
		q = $('#comment_textarea').val();
			if (q.length > 70)
				alert('Seu Tweet precisa ter menos que 70 caracteres!');	
			else
				Dajaxice.main.post_twitter(function callback(data){
				  ('body').html(data.response);
				});
	})
 });