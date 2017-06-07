$(document).ready(function(){

$("#getUserName").keyup(function(event){
    if(event.keyCode == 13){
        $("#ok").click();
    }
});

$('#ok').click(function(){
	$(".card").empty();
	var name = document.getElementById('getUserName').value.split("/").pop();
	var req_url = "/quoracard/"+name ;
	$(".card").load(req_url);

});
});	
