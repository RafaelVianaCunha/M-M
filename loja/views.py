from django.shortcuts import render

# Create your views here.

def index(request):
     return render(request, 'index.html')

def produto(request):
     return render(request, 'produto.html')

def pagamento(request):
     return render(request, 'pagamento.html')