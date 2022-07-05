from django.shortcuts import render


def instalacao(request):
    return render(request, 'paginas/instalacao.html')

def index(request):
    return render(request, 'paginas/index.html')