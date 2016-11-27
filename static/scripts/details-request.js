function requestDetails()
{
	var name = document.getElementById('getUserName').value;
	var req_url = "/quoracard/"+name ;

	$('.mainContent').show();
	$('html,body').animate({
        scrollTop: $(".mainContent").offset().top},
        'slow');
	
	$(".card").load(req_url);
}

$(document).ready(function(){
document.getElementById('ok').addEventListener('click',requestDetails);	
});