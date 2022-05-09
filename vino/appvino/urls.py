from django.contrib import admin
from django.urls import path
from appvino import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('usuarios', views.usuarios, name='Usuarios'),
    path('bodegas', views.bodegas, name='Bodegas'),
    path('vinos', views.vinos, name='Vinos'),
    path('usuariosFormularios', views.usuariosFormulario, name='usuariosFormulario'),
]