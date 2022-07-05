from django.shortcuts import render


def engenharia(request):
    return render(request, 'paginas/engenharia.html')

def index(request):
    return render(request, 'paginas/index.html')
