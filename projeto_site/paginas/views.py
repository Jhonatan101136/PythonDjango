from django.shortcuts import render


def paginas(request):
    return render(request, 'paginas/index.html')


def sobre(request):
    return render(request, 'paginas/sobre.html')




