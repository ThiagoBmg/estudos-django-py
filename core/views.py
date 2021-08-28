from django.shortcuts import render

from .models import Pedido

# Create your views here.
def index(request):
    pedidos = Pedido.objects.all()
    context = {
        'pedidos': pedidos
    }
    return render(request, 'index.html', context)