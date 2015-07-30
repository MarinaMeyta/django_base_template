$(document).ready(function() {
	$('#add_button').click(function () {

		$('#Name').val('');
		$('#Surname').val('');

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
							url: "/persons/add_person/",
							data: {
								'new_name': $('#Name').val(),
								'new_surname': $('#Surname').val()
							},
							success: alertSuccess,
							dataType: 'html'
						});
					}
				}
			]
		});

		function alertSuccess () {
			alert('Человек добавлен');
			// add person into table $('#table').append(html) --- alertSuccess(html)
		};
	});
});
