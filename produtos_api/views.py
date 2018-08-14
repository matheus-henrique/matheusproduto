from django.shortcuts import render,get_object_or_404
from produtos_api.models import Produtos,Fornecedores
from produtos_api.serializers import ProdutosSerializer,FornecedoresSerializer
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import generics
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

class GerarAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

class ProdutoViewSet(viewsets.ModelViewSet):
	serializer_class = ProdutosSerializer
	queryset = Produtos.objects.all()
	filter_backends = (DjangoFilterBackend,)
	filter_fields = ('nome',)

	def get_queryset(self):
		queryset = Produtos.objects.all()
		return queryset.filter(nome=self.request.query_params.get('nome'))

	def update(self, request, pk=None):
		produto = self.get_object(pk)
		serializer = ProdutosSerializer(produto, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)

	def list(self, request):
		search_param = self.request.query_params.get('nome')
		if(search_param):
			queryset = self.get_queryset()
		else:
			queryset = Produtos.objects.all()
		serializer = ProdutosSerializer(queryset, many=True)
		return Response(serializer.data)
	def create(self,request):
		serializer = ProdutosSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)	

	def retrieve(self, request, pk=None):
		queryset = Produtos.objects.all()
		produto = get_object_or_404(queryset, pk=pk)
		serializer = ProdutosSerializer(produto)
		return Response(serializer.data)

	def destroy(self, request, *args, **kwargs):
		try:
			instance = self.get_object()
			self.perform_destroy(instance)
		except Http404:
			pass
		return Response(status=status.HTTP_204_NO_CONTENT)	


class FornecedorViewSet(viewsets.ModelViewSet):
	serializer_class = FornecedoresSerializer
	queryset = Fornecedores.objects.all()
	filter_backends = (DjangoFilterBackend,)
	filter_fields = ('nome',)

	def get_queryset(self):
		queryset = Fornecedores.objects.all()
		return queryset.filter(nome=self.request.query_params.get('nome'))

	def list(self, request):
		search_param = self.request.query_params.get('nome')
		if(search_param):
			queryset = self.get_queryset()
		else:
			queryset = Fornecedores.objects.all()
		serializer = FornecedoresSerializer(queryset, many=True)
		return Response(serializer.data)

	def update(self, request, pk=None):
		fornecedor = self.get_object(pk)
		serializer = ProdutosSerializer(fornecedor, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)

	def retrieve(self, request, pk=None):
		queryset = Fornecedores.objects.all()
		produto = get_object_or_404(queryset, pk=pk)
		serializer = FornecedoresSerializer(produto)
		return Response(serializer.data)

	def create(self,request):
		serializer = FornecedoresSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def destroy(self, request, *args, **kwargs):
		try:
			instance = self.get_object()
			self.perform_destroy(instance)
		except Http404:
			pass
		return Response(status=status.HTTP_204_NO_CONTENT)


