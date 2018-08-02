$(document).ready(function(){
	$.ajax({
		type : "get",
		url: "/produtos/",
		dataType: "json",
		success : function(data){
			$.each(data, function(){
				$("#tbodyprodutos").append(
					"<tr><th scope='row'>"+this.id+"</th><td>"+this.nome+"</td><td> R$"+this.valor+"</td><td><button type='button' class='btn btn-primary'>Editar</button><button type='button' class='btn btn-danger'>Excluir</button></td>");
			})
		}
	});
});


$(document).on('submit',"#form_cadastra_produto", function(e){
	e.preventDefault();
	var nome = $('#nome').val();
	var valor = $('#valor').val();
	$.ajax({
		type : "POST",
		url: "/produtos/",
		dataType: "json",
		contentType: 'application/json',
		data: JSON.stringify({'nome': nome,'valor': valor}),
		success : function(data){
			$("#tbodyprodutos").append(
					"<tr><th scope='row'>"+data.id+"</th><td>"+data.nome+"</td><td> R$"+data.valor+"</td><td><button type='button' class='btn btn-primary'>Editar</button><button type='button' class='btn btn-danger'>Excluir</button></td>");
			$("#msg").html("<div class='alert alert-success' role='alert'>O produto <strong>"+data.nome+"</strong> foi adicionado com <strong>sucesso!!</strong></div>")

		}

	});
});