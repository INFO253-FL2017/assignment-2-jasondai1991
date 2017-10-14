

var form = document.getElementById("contactus");

document.getElementById("name").innerHTML="";
document.getElementById("subject").innerHTML="";
document.getElementById("message").innerHTML="";




form.addEventListener("submit",function(evt){
	var x = new Array();
	var success = "Your message has been sent!";
	var name = document.getElementById("name").value;
	var subject = document.getElementById("subject").value;
	var message = document.getElementById("message").value;
	var display = document.getElementById("display");
	var fail="";
	if(!name){
		fail = fail+"Name ";
	}
	if(!subject){
		fail = fail+"Subject ";
	}
	if(!message){
		fail = fail+"Message ";
	}
	if(fail){
		console.log("form submission cancelled");
		display.innerHTML = fail+"Box need to be filled";
		evt.preventDefault();
	}
	else{console.log(fail+"is being submitt");}
})

// var name1 = document.getElementById("name");
// var subject1 = document.getElementById("subject");
// var message1 = document.getElementById("message");
	
// name1.addEventListener("click",function(){
// 	display.innerHTML="";
// })

// subject1.addEventListener("click",function(){
// 	display.innerHTML="";
// })

// message1.addEventListener("click",function(){
// 	display.innerHTML="";
// })

	
		
	

