$(document).ready(function(){
	$.ajax({
		type : "get",
		url: "/produtos/",
		dataType: "json",
		success : function(data){
			$.each(data, function(){
				$("#tbodyprodutos").append(
					"<tr><th scope='row'>"+this.id+"</th><td>"+this.nome+"</td><td> R$"+this.valor+"</td><td><button type='button' class='btn btn-primary btn-editar' data-value="+this.id+">Editar</button><button type='button' class='btn btn-danger'>Excluir</button></td>");
			})
		}
	});
});


$(document).on('click',"#form-modal", function(event){
	event.preventDefault();
	var nome = $('#modal-nome').val();
	var valor = $('#modal-valor').val();
	var id = $('#modal-id').val();
	$.ajax({
		type : "PUT",
		url: "/produto/"+id+"/",
		dataType: "json",
		contentType: 'application/json',
		data: JSON.stringify({'id':id,'nome': nome,'valor': valor}),
		success : function(data){
			$('.modal').modal('hide');
			$("#msg").html("<div class='alert alert-success' role='alert'>O produto <strong>"+data.nome+"</strong> foi alterado com <strong>sucesso!!</strong></div>");
			location.reload();
		}

	});
});

$(document).on('click','.btn-editar', function(){
	$.ajax({
		type : "get",
		url: "/produto/"+$(this).attr('data-value')+"/",
		dataType: "json",
		success : function(data){
			$('.modal').modal('show');
			$("#modal-nome").val(data.nome);
			$("#modal-valor").val(data.valor);
			$("#modal-id").val(data.id);
		}
	});

});

$(document).on('submit',"#form_cadastra_produto", function(event){
	event.preventDefault();
	alert("cfdasdad");
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
					"<tr><th scope='row'>"+data.id+"</th><td>"+data.nome+"</td><td> R$"+data.valor+"</td><td><button type='button' class='btn btn-primary btn-editar' data-value='"+data.id+">Editar</button><button type='button' class='btn btn-danger'>Excluir</button></td>");
			$("#msg").html("<div class='alert alert-success' role='alert'>O produto <strong>"+data.nome+"</strong> foi adicionado com <strong>sucesso!!</strong></div>")

		}

	});
});
