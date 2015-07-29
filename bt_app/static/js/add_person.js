$(document).ready(function() {
	$('#add_button').click(function () {
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
						alert('Человек добавлен');
					}
				}
			]
		});
	});

});
