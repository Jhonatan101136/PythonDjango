from django.urls import path

from . import views

urlpatterns = [
    path('engenharia_civil/', views.engenharia_civil),
]
