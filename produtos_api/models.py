from django.db import models


class Produtos(models.Model):
	nome = models.TextField()
	valor = models.FloatField()
	def __str__(self):
		return self.nome


class Fornecedores(models.Model):
	nome = models.TextField()
	endereco = models.TextField()
	cnpj = models.TextField()
	produtos = models.ManyToManyField(Produtos, blank=True, default="")

	def __str__(self):
		return self.nome
