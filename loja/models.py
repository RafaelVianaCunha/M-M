#!/usr/bin/python
# -*- coding: UTF-8 -*-

from django.db import models
from django.utils.timezone import now

class Produto(models.Model):
    nome = models.CharField(max_length=255, null=False)
    valor = models.CharField(max_length=255, null=False)
    qtd = models.CharField(max_length=255, null=False)
    tecido = models.CharField(max_length=255, default='Não informado')
    tamanho = models.CharField(max_length=255, default='Não informado')
    fabricante = models.CharField(max_length=255, default='Não informado')
    origem = models.CharField(max_length=255, default='Não informado')
    descricao = models.TextField(default="Não informado")
    dataAdicionado = models.DateField(default=now())
    qtdVendido = models.CharField(max_length=255, default=0)

class Categoria(models.Model):
    nome = models.CharField(max_length=255, null=True)
    descricao = models.CharField(max_length=255, null=True)
    produtos = models.ManyToManyField(Produto, related_name="categorias")

class SubCategoria(models.Model):
    nome = models.CharField(max_length=255, null=True)
    categoria = models.ForeignKey(Categoria, related_name='subCategoria')

class Imagem(models.Model):
    img = models.ImageField(upload_to='img/%Y')
    descricao = models.CharField(max_length=255, null=True)
    produto = models.ForeignKey(Produto, related_name='imagens')

