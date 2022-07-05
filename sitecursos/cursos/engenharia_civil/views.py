from django.shortcuts import render

# Create your views here.
def engenharia_civil(request):
    return render(request, 'paginas/engenharia_civil.html')
