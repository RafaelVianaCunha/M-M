from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.base import View
from loja.models import Produto
from datetime import datetime
from forms import CadastrarProdutoForm


# Create your views here.

def adm(request):
    return render(request, 'adm.html')


class CadastrarProduto(View):
    template_nome = 'adm.html'

    def get(self, request):
        return render(request, self.template_nome)

    def post(self, request):
        form = CadastrarProdutoForm(request.POST)
        if form.is_valid():
            dados_form = form.data
            # Cria o o produto
            produto = Produto(nome=dados_form['nome'])
            # valor=dados_form['valor'],
            # tecido=dados_form['tecido'],
            # tamanho=dados_form['tamanho'],
            # fabricante=dados_form['fabricante'],
            # descricao=dados_form['descricao'],
            # dataAdicionado=datetime.now(),
            # qtdVendido=0)

            produto.save()
            return redirect('adm')
        return render(request, self.template_nome, {'form': form})
