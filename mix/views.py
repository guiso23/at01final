

from django.shortcuts import render, get_object_or_404
from .models import Produto


def home(request):
    
    produtos = Produto.objects.all() 
    context = {
        'produtos': produtos  
    }
    
    return render(request, 'mix/home.html', context)



def detalhe_produto(request, pk):
    
    produto = get_object_or_404(Produto, pk=pk)
    context = {
        'produto': produto 
    }
    
    return render(request, 'mix/detalhe_produto.html', context)