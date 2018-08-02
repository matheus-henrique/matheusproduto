from django.db import models


class Produtos(models.Model):
	nome = models.TextField();
	valor = models.FloatField();

	def __str__(self):
		return self.nome