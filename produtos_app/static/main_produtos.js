$(document).ready(function(){
	$.ajax({
		type : "get",
		url: "/produtos/",
		dataType: "json",
		success : function(data){
			$.each(data, function(){
				$("#tbodyprodutos").append(
					"<tr><th scope='row'>"+this.id+"</th><td>"+this.nome+"</td><td> R$"+this.valor+"</td><td><button type='button' class='btn btn-success'>Editar</button><button type='button' class='btn btn-danger'>Excluir</button></td>");
			})
		}
	});
});