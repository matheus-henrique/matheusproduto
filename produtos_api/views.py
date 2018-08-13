from django.shortcuts import render
from produtos_api.models import Produtos,Fornecedores
from produtos_api.serializers import ProdutosSerializer,FornecedoresSerializer
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status

class ProdutosList(APIView):

	def get(self, request, format=None):
		produtos = Produtos.objects.all()
		serializer = ProdutosSerializer(produtos, many=True)
		return Response(serializer.data)

	def post(self,request):
		print(request.data)
		serializer = ProdutosSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProdutosListDetails(APIView):
	def get_object(self,pk):
		try:
			return Produtos.objects.get(pk=pk)
		except Produtos.DoesNotExist:
			raise Http404	

	def get(self, request,pk,format=None):
		produto = self.get_object(pk)
		serializer = ProdutosSerializer(produto)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		produto = self.get_object(pk)
		serializer = ProdutosSerializer(produto, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)

	def delete(self, request, pk, format=None):
		produto = self.get_object(pk)
		produto.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FornecedoresList(APIView):

	def get(self, request, format=None):
		fornecedores = Fornecedores.objects.all()
		serializer = FornecedoresSerializer(fornecedores, many=True)
		return Response(serializer.data)

	def post(self,request):
		serializer = FornecedoresSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FornecedoresListDetails(APIView):
	def get_object(self,pk):
		try:
			return Fornecedores.objects.get(pk=pk)
		except Produtos.DoesNotExist:
			raise Http404	

	def put(self, request, pk, format=None):
		fornecedor = self.get_object(pk)
		serializer = FornecedoresSerializer(fornecedor, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)


