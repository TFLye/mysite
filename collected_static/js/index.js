$(document).ready(function () {
	//导航栏变化动画
			$(window).scroll(function () {
			     if ($(document).scrollTop() > 80) {
					 $(".top").animate({width: "show"},1000); //IE,FF
					
			      }else {
					  $(".top").animate({width: "hide"},1000); //IE,FF
					 }
			});
		$(function(){
			$("#toTop").click(function(){
			$("html").animate({"scrollTop": "0px"},500); //IE,FF
			$("body").animate({"scrollTop": "0px"},500); //Webkit
        });
     })
});


$(function(){
	if(navigator.userAgent.match(/mobile/i)) {
		top.location='http://m.baidu.com/';
	}
   });


 