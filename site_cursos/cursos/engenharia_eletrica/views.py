from django.shortcuts import render


def engenharia_eletrica(request):
    return render(request, 'paginas/engenharia_eletrica.html')