// $(document).ready(function() {
// 	$("#person_dialog_form").fadeIn('slow');
// });

$(document).ready(function() {
	$( "#dialog" ).dialog({
		// autoOpen: false;
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

	$('#add_button').click(function () {
		$('#add_button').fadeIn('slow', 0);
	});
});
