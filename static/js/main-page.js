// JavaScript Document
change = 0;
function main()
{
	if ( change == 0 )
	{
		var value = screen.width;
		change = 1;
	}
	value = value - 15;
	document.getElementById("topbar").style.width = value + "px";
	document.getElementById("main").style.width = value + "px";
	document.getElementById("left-frame").style.width = ( value * 0.15 ) + "px";
	document.getElementById("right-frame").style.width = ( value * 0.84 ) + "px";
}