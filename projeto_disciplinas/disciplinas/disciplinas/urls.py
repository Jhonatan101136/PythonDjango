"""disciplinas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('primeiro_periodo/', include("primeiro_periodo.urls")),
    path('segundo_periodo/', include("segundo_periodo.urls")),
    path('terceiro_periodo/', include("terceiro_periodo.urls")),
    path('quarto_periodo/', include("quarto_periodo.urls")),
    path('quinto_periodo/', include("quinto_periodo.urls")),
    path('sexto_periodo/', include("sexto_periodo.urls")),
    path('setimo_periodo/', include("setimo_periodo.urls")),
    path('oitavo_periodo/', include("oitavo_periodo.urls")),
]
