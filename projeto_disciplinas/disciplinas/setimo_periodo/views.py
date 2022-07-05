from django.shortcuts import render


def setimo_periodo(request):
    return render(request, 'setimo_periodo/index.html', )
