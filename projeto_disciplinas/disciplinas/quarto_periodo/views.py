from django.shortcuts import render


def quarto_periodo(request):
    return render(request, 'quarto_periodo/index.html', )