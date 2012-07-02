$(document).ready(function(){
	$('#comment_submit').click(function() {
		q = $('#comment_textarea').val();
			if (q.length > 70)
				alert(q);	
			else
				alert(q)
				$(document).load('post_twitter/?text='+q);
	})
 });


