// JavaScript Document
function postorder(type)
  {
      if ((type == "enter" && (event.keyCode==13)) || type == "click")
      {
	  var order = document.getElementById("cmdline").value;
      //clear order
      document.getElementById("cmdline").value = '';
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
  }
function setscrolldown(){
var c = window.document.body.scrollHeight;
window.scroll(0,c); 
}