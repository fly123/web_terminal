var appnum=0;
function open_app(app_div)
{
	var tmp=app_div;
	var path=$(app_div).attr('path');
	var app_name=det_app(path)
	switch (app_name)
	{
		case 'txt':{
			notepad_creat();
			break;}
	}
	/*var tmp="#a+"+tmp.id;
	alert(tmp);
	var path=$('#aapp1').attr('href')
	alert(path);*/
}
function det_app(app_path)
{
	var tmp=Array();
	var app_name;
	tmp=app_path.split('.');
	if(tmp[1])
	{
		app_name=tmp.pop();
	}
	else
	{ 
		return 'no app matched!!';
	}
	if(app_name.indexOf('txt')>-1)
	{
		return 'txt';
	}
	else 
	{
		return app_name;
	}
}
function notepad_creat()
{
	$('#notepad_result').load('/static/tpls/notepad.html');
	$('div.notepad').draggable();
			
}
function notepad_close(notepad)
{
	var sel='#'+notepad.id;
	$(sel).hide('fast');
}
/*
function ajax_request()
{
	if(window.XMLHttpRequest)
	{
		var ohttp=new XMLHttpRequest();
		return ohttp;
	}
	else if(i=2)
	{
	}
	return false;
}*/
$(document).ready(function(){
	$('#app_board').load('/static/tpls/appbutton.html');
	$('div.appbutton').draggable();
	/*$('#test').click(
		function()
		{
			$('div.notepad').resizable({
				maxHeight: 700,
				maxWidth: 1300,
				minHeight: 250,
				minWidth: 300,
				alsoResize: ".notepad_body",
			});
		}
	)*/
});
