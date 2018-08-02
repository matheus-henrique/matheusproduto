from django.db import models

# Create your models here.
class Produtos(models.Model):
	nome = models.TextField();
	valor = models.FloatField();


	def __str__(self):
		return self.nome