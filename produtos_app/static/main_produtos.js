$(document).ready(function(){
	$.ajax({
		type : "get",
		url: "api/v1/produtos/",
		dataType: "json",
		success : function(data){
			$.each(data, function(){
				$("#tbodyprodutos").append("<tr class=produto"+this.id+" id='produto'><th scope='row'>"+this.id+"</th><td>"+this.nome+"</td><td> R$"+this.valor+"</td><td><button type='button' class='btn btn-primary btn-editar' data-value="+this.id+">Editar</button><button type='button' class='btn btn-danger btn-excluir' data-value="+this.id+">Excluir</button></td>");
			});
			verifica_tem_produto_cadastrado();

		}
	});
});


$(document).on('submit',"#form_cadastra_produto", function(event){
	event.preventDefault();
	var nome = $('#nome').val();
	var valor = $('#valor').val();
	$.ajax({
		type : "POST",
		url: "api/v1/produtos/",
		dataType: "json",
		contentType: 'application/json',
		data: JSON.stringify({'nome': nome,'valor': valor}),
		beforeSend: function(xhr) {
        	xhr.setRequestHeader('X-CSRFToken', Cookies.get('csrftoken'))
   		},
		success : function(data){
			$("#tbodyprodutos").append(
					"<tr class=produto"+data.id+" id='produto'><th scope='row'>"+data.id+"</th><td>"+data.nome+"</td><td> R$"+data.valor+"</td><td><button type='button' class='btn btn-primary btn-editar' data-value='"+data.id+"'>Editar</button><button type='button' class='btn btn-danger btn-excluir' data-value="+data.id+">Excluir</button></td>");
			$("#msg").html("<div class='alert alert-success' role='alert'>O produto <strong>"+data.nome+"</strong> foi adicionado com <strong>sucesso!!</strong></div>")
			verifica_tem_produto_cadastrado();

		},
		error : function(){
			$("#msg").html("<div class='alert alert-danger' role='alert'>Verifique o campo <strong>Valor do Produto</strong> ele só aceita tipos <strong>numericos</strong>.</div>");
		}

	});
});


$(document).on('submit',"#form_login", function(event){
	var formdata = new FormData($("form[name='login-form']")[0]);
	event.preventDefault();
	$.ajax({
		type : "POST",
		url: "criar-usuario/",
		data: formdata,
		processData: false,
        contentType: false,
		success : function(data){

		},
		error : function(){

		}

	});
});


$(document).on('submit',"#form-modal", function(event){
	event.preventDefault();
	var nome = $('#modal-nome').val();
	var valor = $('#modal-valor').val();
	var id = $('#modal-id').val();
	$.ajax({
		type : "PUT",
		url: "api/v1/produtos/"+id+"/",
		dataType: "json",
		contentType: 'application/json',
		data: JSON.stringify({'id':id,'nome': nome,'valor': valor}),
		beforeSend: function(xhr) {
        	xhr.setRequestHeader('X-CSRFToken', Cookies.get('csrftoken'))
   		},
		success : function(data){
			$('.modal').modal('hide');
			$("#msg").html("<div class='alert alert-success' role='alert'>O produto <strong>"+data.nome+"</strong> foi alterado com <strong>sucesso!!</strong></div>");
			location.reload();
		},
		error : function(){
			$('.modal').modal('hide');
			$("#msg").html("<div class='alert alert-danger' role='alert'>Verifique o campo <strong>Valor do Produto</strong> ele só aceita tipos <strong>numericos</strong>.</div>");
		}

	});
});


function verifica_tem_produto_cadastrado(){
	var $produto = $('#produto');
	console.log('fasfasf');
	 if (!$produto.length){
	     $("#alert").show();
	     $(".table-produto").hide();
	 }else{
	 	$("#alert").hide();
	 	 $(".table-produto").show();
	 }
}

$(document).on('click','.btn-excluir', function(){
	var id = $(this).attr('data-value'); 
	$.ajax({
		type : "DELETE",
		url: "api/v1/produtos/"+id+"/",
		dataType: "json",
		contentType: 'application/json',
		data: JSON.stringify({'id':id,'nome': nome,'valor': valor}),
		beforeSend: function(xhr) {
        	xhr.setRequestHeader('X-CSRFToken', Cookies.get('csrftoken'))
   		},
		success : function(data){
			var $target = $(".produto"+id);
			$(".produto"+id).remove();
			verifica_tem_produto_cadastrado();
		},
		error : function(){
			var $target = $(".produto"+id);
			$(".produto"+id).remove();
			verifica_tem_produto_cadastrado();
		}

	});
	
});

$(document).on('click','.btn-editar', function(){
	$.ajax({
		type : "get",
		url: "api/v1/produtos/"+$(this).attr('data-value')+"/",
		dataType: "json",
		success : function(data){
			$('.modal').modal('show');
			$("#modal-nome").val(data.nome);
			$("#modal-valor").val(data.valor);
			$("#modal-id").val(data.id);
		}
	});

});

