$(document).ready(function() {
	$('#add_button').click(function () {

		$('#Name').val('');
		$('#Surname').val('');


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
			title: "Добавить человека",
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
							url: "/add_person/",
							data: { 'serialized_data': $('#person_dialog_form').serialize()} 
							,
							success: alertSuccess(),
							dataType: 'html'
						});
					}
				}
			]
		});

		function alertSuccess () {
			alert('Человек добавлен');
			document.location.reload();

			//$("#content_with_table").html(data);
			// add person into table $('#table').append(html) --- alertSuccess(html)
		};
	});
});
