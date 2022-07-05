from django.urls import path

from . import views

urlpatterns = [
    path('engenharia_mecanica/', views.engenharia_mecanica),
]
