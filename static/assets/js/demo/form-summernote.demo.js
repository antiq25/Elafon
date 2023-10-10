/*
Template Name: ADMETRO - Responsive Admin Template Built with Bootstrap 4
Version: 1.0.0
Author: Sean Ngu
Website: http://www.seantheme.com/admetro-v1.0/
*/

var handleRenderSummernote = function() {
	var totalHeight = $(window).height() - $('.summernote').offset().top - 155;
	$('.summernote').summernote({
		height: totalHeight
	});
};


/* Controller
------------------------------------------------ */
$(document).ready(function() {
	handleRenderSummernote();
});