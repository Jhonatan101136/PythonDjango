from django.shortcuts import render


def ambiente(request):
    return render(request, 'paginas/ambiente.html')

def index(request):
    return render(request, 'paginas/index.html')