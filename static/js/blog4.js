var submit = document.getElementById("submit");
var display = document.getElementById("comment-dis");

submit.addEventListener("click",function(event){
	var name = document.getElementById("name").value;
	var comment =document.getElementById("comment").value;
	localStorage.setItem(name,comment);
	localStorage.setItem("lastkey4",name);
	display.innerHTML = localStorage.getItem("lastkey4")+" wrote: "+localStorage.getItem(localStorage.getItem("lastkey4"));
	document.getElementById("name").value="";
	document.getElementById("comment").value="";
	event.preventDefault();
})

display.innerHTML = localStorage.getItem("lastkey4")+" wrote: "+localStorage.getItem(localStorage.getItem("lastkey4"));


function getweather(){
	var xmlhttp=new XMLHttpRequest();
	url="http://api.openweathermap.org/data/2.5/weather?id=5327684&&APPID=b83d0ffca572c6ca605ef0ef0d63b188&units=imperial";
	xmlhttp.open("POST",url,false);
	xmlhttp.send();
	document.getElementById("myDiv").innerHTML=JSON.parse(xmlhttp.responseText).weather[0].main+",  "+JSON.parse(xmlhttp.responseText).main.temp+" °F";
}

window.setInterval(getweather(), 2000);