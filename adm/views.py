from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.base import View
from loja.models import Produto, Categoria, SubCategoria, Imagem
from datetime import datetime
from forms import CadastrarProdutoForm, CategoriaForm, SubCategoriaForm



def base(request):
    return render(request, 'baseAdm.html')


class CadastrarProduto(View):
    template_nome = 'produtoAdm.html'

    def get(self, request):
        return render(request, self.template_nome, {'categorias': Categoria.objects.all()})

    def post(self, request):
        form = CadastrarProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            dados_form = form.data
            # Cria o o produto
            produto = Produto(nome=dados_form['nome'],
                              valor=dados_form['valor'],
                              qtd=dados_form['qtd'],
                              tecido=dados_form['tecido'],
                              tamanho=dados_form['tamanho'],
                              fabricante=dados_form['fabricante'],
                              origem=dados_form['origem'],
                              descricao=dados_form['descricao'],
                              dataAdicionado=datetime.now(),
                              qtdVendido=0)
            produto.save()
            # salva o produto na categoria
            categoria = Categoria.objects.get(id=dados_form['categoria'])
            categoria.produtos.add(produto)
            categoria.save()
            # Cria a img do produto
            img = Imagem(img=request.FILES['img'],
                         descricao=dados_form["desImg"],
                         produto=produto)
            img.save()
            return redirect('produto')

        return render(request, self.template_nome, {'form': form, 'categorias': Categoria.objects.all()})


class CategoriaView(View):
    template_nome = 'categoriaAdm.html'

    def get(self, request):
        return render(request, self.template_nome)

    def post(self, request):
        form = CategoriaForm(request.POST)
        if form.is_valid():
            dados_form = form.data

            # Cria a categoria
            categoria = Categoria(nome=dados_form['nome'],
                                  descricao=dados_form['descricao'])
            categoria.save()
            return redirect(categoria)
        return render(request, self.template_nome, {'form': form})


class SubCategoriaView(View):
    template_nome = 'subCategoriaAdm.html'

    def get(self, request):
        return render(request, self.template_nome, {'categorias': Categoria.objects.all()})

    def post(self, request):
        form = SubCategoriaForm(request.POST)
        if form.is_valid():
            dados_form = form.data
            # Cria a Subcategoria
            subCat = SubCategoria(nome=dados_form['nome'],
                                  categoria=Categoria.objects.get(id=dados_form['categoria']))
            subCat.save()

            print(subCat.nome)
            print(subCat.categoria.nome)

            return redirect('subCategoria')
        return render(request, self.template_nome, {'form': form, 'categorias': Categoria.objects.all()})
