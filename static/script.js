$(document).ready(function() {
	$(document).on('click', '.remove', function(){
		$(this).parent().remove();
		})
	

	$(document).on('click', '.checkbox', function(){
		$(this).parent().addClass('completed');

		$(this).attr('disabled', true);
		
		var uid = $(this).attr('data-uid');
		$.get('/api/comlete/' + uid);
		//console.log("Запрос")
	});
})
