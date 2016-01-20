from django.shortcuts import render
from models import Produto
from models import Categoria, Produto

# Create your views here.

def index(request):
     return render(request, 'index.html', { 'categorias' : Categoria.objects.all(), 'produtos' : Produto.objects.all()})

def produto(request):
     return render(request, 'produto.html')

def pagamento(request):
     return render(request, 'pagamento.html')