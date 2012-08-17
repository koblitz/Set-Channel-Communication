 
 $(document).ready(function(){
	$('#comment_submit').submit(function() {
		q = $('#comment_textarea').val();
			if (q.length > 70)
				alert('Seu Tweet precisa ter menos que 70 caracteres!');	
			else
				  $.ajax({
					    type: "GET",
                                            url:"post_twitter/",
					    data:{
                                                   'text':q,
                                                 },
                                            success: function(data){
                                                       $('body').html(data);
                                                          }
                                        });
	})
 });