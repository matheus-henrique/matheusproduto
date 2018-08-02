from rest_framework import serializers
from produtos_api.models import Produtos

class ProdutosSerializer(serializers.ModelSerializer):
	class Meta:
		model = Produtos
		fields = ('id','nome','valor')
