"""
URL configuration for musicbox project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from musicboxWebApp import views


urlpatterns = [
    path("",views.login, name="login"),
    path("inicio/<nombre_usuario>/",views.inicio, name="inicio"),
    path("buscar/",views.buscar),
    path("iniciar/",views.iniciar),
    path("crear_lista/",views.crear_lista),
    path("incorporar_album/",views.incorporar_album),
    path('detalle_album/<album>/<nombre_usuario>/', views.detalle_album, name="detalle_album"),
    path("listas/<nombre_usuario>/",views.listas, name="listas"),
    path("detalle_lista/<lista_nombre>/<nombre_usuario>/",views.detalle_lista, name="detalle_lista"),
]
