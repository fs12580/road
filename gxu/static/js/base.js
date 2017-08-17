$(function(){
	// var width = $(".slider").find(".slider-item").width();
	// var length = $(".slider").find(".slider-item").length;
	// $(".slider-wrapper").width(width*length);
	$(".slider").find(".slider-item").eq(0).addClass("active");
	$(".slider").find(".in-tro li").eq(0).addClass("active");
	$(".slider").find(".in-tro li").each(function(index){
		$(this).mouseover(function(){
			$(".slider").find(".slider-item").removeClass("active");
			$(".slider").find(".slider-item").eq(index).addClass("active");
			$(".slider").find(".in-tro li").removeClass("active");
			$(".slider").find(".in-tro li").eq(index).addClass("active");
		})
	})
})