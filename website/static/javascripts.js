"use strict";

$(document).ready(function(){
	$("#id_city").prop('disabled', true);
});

$( "#id_local_delivery" ).click(function() {
	if ($("#id_local_delivery").is(":checked")){
		$("#id_city").prop('disabled', false);
	}
	else {
		$("#id_city").prop('disabled', true);
	}
});
		

