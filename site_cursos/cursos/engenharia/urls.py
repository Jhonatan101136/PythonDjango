from django.urls import path

from . import views

urlpatterns = {
    path('engenharia_software/', views.engenharia),
    path('index', views.index),


}