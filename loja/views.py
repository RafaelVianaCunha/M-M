from django.shortcuts import render
from models import Produto

# Create your views here.

def index(request):
     return render(request, 'index.html', { 'produtos' : Produto.objects.all()})

def produto(request):
     return render(request, 'produto.html')

def pagamento(request):
     return render(request, 'pagamento.html')