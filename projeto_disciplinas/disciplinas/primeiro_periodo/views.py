from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def primeiro_periodo(request):
    return render(request, 'primeiro_periodo/index.html', )