var appnum=0;
function open_app(app_div)
{

	var path=$(app_div).attr('path');
	var app_name=det_app(path)
	switch (app_name)
	{
		case 'txt':{
			notepad_creat();
			break;}
	}
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
}
function notepad_close(notepad)
{
	var sel='#'+notepad.id;
	$(sel).hide('fast');
}
//未实现迭代前的实验函数
function drag1(div)
{
	//$('div').not('#app1').css('z-index','-1');
	$(div).draggable({
		grid: [ 78, 91 ],
	containment: "#app_board", 
	scroll: false 
	});
	
}
//使notepad可移动和可变化大小
function pad_drag(div)
{
	//$('div').not('#notepad1').css('z-index','-1');
	if(!is_draggable($(div)))
	{
		$(div).draggable({
		containment: "#notepad_result", 
		scroll: false 
		});
		$(div).resizable({
				maxHeight: 700,
				maxWidth: 1300,
				minHeight: 250,
				minWidth: 300,
				alsoResize: ".notepad_body",
		});
	}
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
function is_draggable(div)
{
	var tmpdiv=div[0];
	var classname=tmpdiv.className;
	if(classname.indexOf('ui-draggable')>-1)
	{
		return 1;
	}else 
	{
		return false;
	}
}
$(document).ready(function(){
	$('#app_board').load('/static/tpls/appbutton.html');
	$('div.appbutton').draggable({
	containment: "#app_board", 
	scroll: false 
	});
	//后台迭代后开启此绑定函数
	/*$('div.appbutton').bind('mouseover',function(){
		if(!is_draggable($(this))){
			$(this).draggable({
				grid: [ 78, 91 ],
				containment: "#app_board", 
				scroll: false 
				});
			}
		}
	);*/
});
