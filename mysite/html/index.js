 $(document).ready(function(){
 	$('#comment_submit').submit(function() {
 	        Dajaxice.views.post_twitter(post_callback);
 				 	})
  });
  
  function callback(data){
    body.html(data);
  }
 
 
