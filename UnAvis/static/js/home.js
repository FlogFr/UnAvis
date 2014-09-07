
$(document).ready(function(){

	$("[rel='tooltip']").tooltip();

	$(".thumbnail").hover(
		function(){
			$(this).find('.caption').fadeIn(250);
		},
		function(){
			$(this).find('.caption').fadeOut(150);
		}
	);

})
