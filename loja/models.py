from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=255, null=False)
    valor = models.CharField(max_length=255, null=True)
    qtd = models.PositiveIntegerField(null=True)
    descricao = models.TextField(null=True)
    dataAdicionado = models.DateField(null=True)
    qtdVendido = models.PositiveIntegerField(null=True)

class Categoria(models.Model):
    nome = models.CharField(max_length=255, null=True)
    descricao = models.CharField(max_length=255, null=True)
    produtos = models.ManyToManyField(Produto, related_name="categorias")

class SubCategoria(models.Model):
    nome = models.CharField(max_length=255, null=True)
    categoria = models.ForeignKey(Categoria, related_name='subCategoria')

class Imagem(models.Model):
    img = models.FileField(upload_to='img/%Y')
    descricao = models.CharField(max_length=255, null=True)
    produto = models.ForeignKey(Produto, related_name='imagens')