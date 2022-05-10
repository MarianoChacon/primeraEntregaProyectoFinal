from django.contrib import admin
from django.urls import path
from appvino import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('usuarios', views.usuarios, name='Usuarios'),
    path('bodegas', views.bodegas, name='Bodegas'),
    path('vinos', views.vinos, name='Vinos'),
    path('usuariosFormularios', views.usuariosFormulario, name='usuariosFormulario'),
    path('ingresoCorrecto', views.ingresoCorrecto, name='ingresoCorrecto'),
    path('vinosFormularios', views.vinosFormulario, name='vinosFormulario'),
    path('bodegasFormularios', views.bodegasFormulario, name='bodegasFormulario'),
    path('busquedaUsuario', views.busquedaUsuario, name='busquedaUsuario'),
    path('buscar/', views.buscar, name='buscar'),
]