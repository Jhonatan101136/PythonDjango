from django.urls import path

from . import views

urlpatterns = [
    path('engenharia_automacao/', views.engenharia_automacao),
]
