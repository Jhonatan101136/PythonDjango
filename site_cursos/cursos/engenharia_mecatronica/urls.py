from django.urls import path

from . import views

urlpatterns = [
    path('engenharia_mecatronica/', views.engenharia_mecatronica),
]
