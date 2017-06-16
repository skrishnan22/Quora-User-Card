$(document).ready(function(){

$("#getUserName").keyup(function(event){
    if(event.keyCode == 13){
        update();
    }
});

$('#ok').click(update);
	
function update(){
	$(".card").empty();
	var name = document.getElementById('getUserName').value.split("/").pop();
	var req_url = "/quoracard/"+name ;
	$(".card").load(req_url);
}
	
});	
