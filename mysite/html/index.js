$(document).ready(function(){
		
		$('#comment_submit').click(function() {
		q = $('#comment_textarea').val();
			if (q.length > 70)
				alert('Seu tweet precisa ter \n menos que 70 caracteres.');	
			else{
				$.load('/twitter/?text='+q); 
			        alert('seu tweet foi publicado'); }
			         
				
			})
     			});


