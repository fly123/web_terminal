// JavaScript Document
x=0;
function platform()
{
	if ( x == 0 )
	{
		var ListNode = document.getElementById("response");
		platform = ListNode.innerHTML;
		if ( platform == "system is Windows" )
		{
			document.body.style.backgroundImage = "url(../static/resourse/microsoft-mascot.png)";
			x = 1;
		}
		if ( platform == "system is Linux" )
		{
			document.body.style.backgroundImage = "url(../static/resourse/linux-mascot.png)";
			x = 1;
		}
	}
}

function postorder()
  {
      if (event.keyCode==13)
      {
	  var order = document.getElementById("cmdline").value;
      //clear order
      document.getElementById("cmdline").value = '';
	  var ListNode = document.getElementById("response");
	  var xmlHttp = new XMLHttpRequest();
	  var url = "/receiveorder";
	  xmlHttp.onreadystatechange=function() {
	  	ListNode.innerHTML = xmlHttp.responseText;
	  	setscrolldown();
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
