from django.shortcuts import render
from provas.models import duvidas

# Create your views here.
def index(request):
    return render(request, 'index.html')


def contato(request):

    return render(request, 'contato.html')


def sobre(request):
    listadeduvidas = duvidas.objects.all()
    context = {
        'duvida': listadeduvidas
    }

    return render(request, 'sobre.html', context)


def localizacao(request):
    return render(request, 'localizacao.html')
