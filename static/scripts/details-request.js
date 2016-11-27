$(document).ready(function(){

$("#getUserName").keyup(function(event){
    if(event.keyCode == 13){
        $("#ok").click();
    }
});

$('#ok').click(function(){
	var name = document.getElementById('getUserName').value.split("/").pop();
	var req_url = "/quoracard/"+name ;
	$('.mainContent').show();
	$('html,body').animate({
        scrollTop: $(".mainContent").offset().top},
        'slow');
	$(".card").load(req_url);

});
});	
