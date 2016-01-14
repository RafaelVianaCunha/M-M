from django.db import models


# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=255, null=False)
    valor = models.CharField(max_length=255, null=True)
    tecido = models.CharField(max_length=255, null=True)
    tamanho = models.CharField(max_length=255, null=True)
    fabricante = models.CharField(max_length=255, null=True)
    qtd = models.PositiveIntegerField(null=True)
    descricao = models.TextField(null=True)
    #   categoria = models.ManyToManyField(Categoria, related_name="categorias")
    #    img = models.ManyToManyField(Imagem, related_name="imagens")
    dataAdicionado = models.DateField(null=True)
    qtdVendido = models.PositiveIntegerField(null=True)


class Categoria(models.Model):
    nome = models.CharField(max_length=255, null=True)


class Imagem(models.Model):
    descricao = models.CharField(max_length=255, null=True)
    pass
