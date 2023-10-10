/*
Template Name: ADMETRO - Responsive Admin Template Built with Bootstrap 4
Version: 1.0.0
Author: Sean Ngu
Website: http://www.seantheme.com/admetro-v1.0/
*/

var handleNotification = function() {
	$.notification({
		title: 'New Mail',
		content: 'You have 20+ new mail in your Inbox',
		icon: 'fa fa-envelope',
		iconClass: 'bg-gradient-blue-indigo text-white'
	});
};


/* Controller
------------------------------------------------ */
$(document).ready(function() {
	handleNotification();
});