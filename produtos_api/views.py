from django.shortcuts import render
from produtos_api.models import Produtos
from produtos_api.serializers import ProdutosSerializer
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response

# Create your views here.
class ProdutosList(APIView):

	def get(self, request, format=None):
		produtos = Produtos.objects.all()
		serializer = ProdutosSerializer(produtos, many=True)
		return Response(serializer.data)

	def delete(self, request, pk, format=None):
		produto = self.get_object(pk)
		produto.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


class ProdutosListDetails(APIView):
	def get_object(self,pk ):
		try:
			return Produtos.objects.get(pk=pk)
		except Produtos.DoesNotExist:
			raise Http404	

	def get(self, request,pk,format=None):
		produto = self.get_object(pk)
		serializer = ProdutosSerializer(produto)
		return Response(serializer.data)
