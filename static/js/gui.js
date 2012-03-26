var next_notepad=0;
var notepad_cache=Array();
function notepad_class(id,context)
{
	this.id=id;
	this.contxt=context;
}
function open_app(app_div)
{
	var path=$(app_div).attr('path');
	var app_type=det_apptype(path);
	var app_name=det_appname(path);
	switch (app_type)
	{
		case '':
		case 'txt':{
			notepad_creat(app_name);
			break;}
		default:{
			alert('无法匹配文件格式');}
	}
}
function det_apptype(app_path)
{
	var tmp=Array();
	var app_type;
	tmp=app_path.split('.');
	if(tmp[1])
	{
		app_type=tmp.pop();
		return app_type;
	}
	else
	{ 
		return false;
	}
}
function det_appname(app_path)
{
	var app_name=app_path.substr(app_path.lastIndexOf("\\")+1);
	if(app_name)
	{
		return app_name;
	}
	else return false;
}
function notepad_creat(app_name)
{
	var id=next_notepad;
	var url='/static/tpls/notepad.html';
	$.get(url,'',function(data,textStatus){
			var id_notepad="id=\"notepad"+id+"\"";
			data=data.replace("id=\"notepad\"",id_notepad);
			var id_context="name=\"notepad_context"+id+"\"";
			data=data.replace("id=\"notepad_context\"",id_context);
			$('#notepad_result').append(data);
			next_notepad++;
			});	
	notepad_cache[id]=new notepad_class(id,"test context");
	//next_notepad++;
}
function notepad_close(notepad)
{
	var div=notepad.parentNode.parentNode;
	var id=div.id;
	var sel='#'+id;
	$(sel).remove();
	//$(sel).remove();
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

/*function ajax_request()
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
