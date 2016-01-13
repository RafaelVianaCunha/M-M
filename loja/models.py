from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=255, null=False)
    descricao = models.CharField(max_length=15, null=False)
    valor = models.CharField(max_length=255, null=False)
    qtd = models.PositiveIntegerField(null=False)
    descricao = models.TextField(null=False)
    categoria = models.ManyToManyField(Categoria, related_name="categorias")
    img = models.ManyToManyField(Imagem, related_name="imagens")
    dataAdicionado = models.DateField(null=False)
    qtdVendido = models.PositiveIntegerField(null=False)

class Categoria(models.Model):
    nome = models.CharField(max_length=255, null=False)

class Imagem(models.Model):
    descricao = models.CharField(max_length=255, null=False)