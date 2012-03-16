// JavaScript Document
function FormExam(Form)
  {
	  var us = Form.account.value;
	  var pw = Form.password.value;
	  var xmlHttp = new XMLHttpRequest();
	  var url = "/login";
	  xmlHttp.onreadystatechange=function()
	  {
		if (xmlHttp.readyState==4) 
		{
			if(xmlHttp.responseText=="1")
			{
				//window.location.reload();
				window.open("/","_self");
				return true;
			}
			else
			{
				if(xmlHttp.responseText=="0")
				{
					document.getElementById("accoutn-error").style.visibility = "visible";
				}
				else
				{
					document.getElementById("password-error").style.visibility = "visible";
				}
				return false;
			}
		}
	  }
	  xmlHttp.open("POST",url,true);
	  xmlHttp.setRequestHeader("Content-Type","application/x-www-form-urlencoded"); 
	  xmlHttp.send("username="+us+"&password="+pw);
	  
	  return false;
  }
