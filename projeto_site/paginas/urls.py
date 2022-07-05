from django.urls import path
from . import views

urlpatterns = [
     path('', views.paginas),
     path('sobre/',views.sobre),

    # path ('', views.index, name='index'),
    # path('sobre/',views.sobre,name='sobre'),

]
