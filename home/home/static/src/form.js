function bind_all(){
	$(".button").click(
		function(){
			activate(this);
			if ($(this).attr("id") == "login_menu"){
				$("#login_form").fadeIn();
			} else{
				$("#login_form").slideUp();
			}
			console.log('dddd');
		}
	);
}

function activate(element){
	deactivate_all();
	$(element).addClass("selected");
}

function deactivate_all(){
	$(".button").removeClass("selected");
}
