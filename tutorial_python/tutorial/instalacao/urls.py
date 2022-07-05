from django.urls import path

from . import views

urlpatterns = {
    path('instalacao/', views.instalacao),
    path('', views.index),


}