// JavaScript Document
function postorder()
  {
	  var order = document.getElementById("order").value;
	  var ListNode = document.getElementById("response");
	  var xmlHttp = new XMLHttpRequest();
	  var url = "/receiveorder";
	  xmlHttp.onreadystatechange=function() {
	  	ListNode.innerHTML = xmlHttp.responseText;
	  	return true;
	  	}
	  xmlHttp.open("POST",url,true);
	  xmlHttp.setRequestHeader("Content-Type","application/x-www-form-urlencoded"); 
	  xmlHttp.send("order="+order);
  }
