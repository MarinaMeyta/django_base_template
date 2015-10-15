$(document).ready(function() {
	$('#add_button').click(function () {

		$('#Point_ID').val('');
		$('#Location').val('');
		$('#IP_address').val('');
		$('#Type').val('');
		$('#Node_ID').val('');
		$('#Notes').val('');
		

		//--------- magic csrf code!---------//
		function getCookie(name) {
		    var cookieValue = null;
		    if (document.cookie && document.cookie != '') {
		        var cookies = document.cookie.split(';');
		        for (var i = 0; i < cookies.length; i++) {
		            var cookie = jQuery.trim(cookies[i]);
		            // Does this cookie string begin with the name we want?
		            if (cookie.substring(0, name.length + 1) == (name + '=')) {
		                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
		                break;
		            }
		        }
		    }
		    return cookieValue;
		}
		var csrftoken = getCookie('csrftoken');

		function csrfSafeMethod(method) {
		    // these HTTP methods do not require CSRF protection
		    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
		}
		$.ajaxSetup({
		    beforeSend: function(xhr, settings) {
		        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
		            xhr.setRequestHeader("X-CSRFToken", csrftoken);
		        }
		    }
		});
		//--------- magic csrf code!---------//


		$( "#dialog" ).dialog({
			title: "Добавить объект кап.строительства",
			width: 500,
			heigth: 200,
			modal: true,
			draggable: false,
			buttons: [
				{
					text: 'Добавить',
					click: function() {
						$.ajax({
							type: "POST",
							url: "/add_object/",
							data: { 'serialized_data': $('#adding_form').serialize()} 
							,
							success: alertSuccess(),
							dataType: 'html'
						});
					}
				}
			]
		});

		function alertSuccess () {
			alert('Объект добавлен');
			location.reload();
		};
	});
});
