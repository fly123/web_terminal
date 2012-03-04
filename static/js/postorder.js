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
		var instruction = document.getElementById("cmdline").value;
      	//clear instruction
      	document.getElementById("cmdline").value = '';
      	if ( instruction.slice(0,6) == "upload" ) {
				  document.getElementById("order").value = instruction;
				  document.getElementById("fileUpload").click();
	  	}
	  	else
	  	{
			var url = "/receiveorder";
			var xmlHttp = new XMLHttpRequest();
			if ( instruction.slice(0,8) == "download" )
			{
			 	 site = getIPAdress();
			 	 xmlHttp.onreadystatechange = function()
				{    
             	 	if ( xmlHttp.readyState == 4 )
              		{
			   			site = site + xmlHttp.responseText;
			    		window.open(site,"_self");
              		}
					return true;
				}
			}
	  		else
	  		{
	  			var ListNode = document.getElementById("response");
	 			var url = "/receiveorder";
	 			xmlHttp.onreadystatechange=function()
				{
	  				ListNode.innerHTML = xmlHttp.responseText;
            		setscrolldown();
	  				return true;
	  			}
      		}
      		xmlHttp.open("POST",url,true);
	 		xmlHttp.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
	 		xmlHttp.send("order=" + instruction);
	  	}
  	}
}
  
function setscrolldown()
{
	var c = window.document.body.scrollHeight;
	window.scroll(0,c); 
}

function uploadfile()
{
    document.getElementById("uploadForm").submit();
}
function getIPAdress()
{
    var rslt="";
    var obj = null;
    try{
    obj = new ActiveXObject("rcbdyctl.Setting");
    rslt = obj.getIPAdress();
    obj = null;
    }
    catch(e)
    {
    }
    return rslt;
}
