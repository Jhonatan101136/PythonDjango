from django.urls import path

from . import views

urlpatterns = [
    path('engenharia_eletrica/', views.engenharia_eletrica),
]
