from rest_framework import serializers
from produtos_api.models import Produtos,Fornecedores

class ProdutosSerializer(serializers.ModelSerializer):
	#id = serializers.ModelField(model_field=Produtos()._meta.get_field('id'))
	class Meta:
		model = Produtos
		fields = ('id','nome','valor')

class FornecedoresSerializer(serializers.ModelSerializer):
	produtos = ProdutosSerializer(many=True)
	class Meta:
		model = Fornecedores
		fields = ('id','nome','endereco','cnpj','produtos')

	
	def update(self, instace, validated_data):
		produtos_data = validated_data.pop('produtos')
		fornecedor = Fornecedores.objects.get(id=instace.id)
		fornecedor.produtos.clear()
		for produto in produtos_data:
			if Produtos.objects.filter(pk=produto['id']).exists():
				fornecedor.produtos.add(Produtos.objects.get(pk=produto['id']))	
		fornecedor.save()
		instace.save()
		return instace