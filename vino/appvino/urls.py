from django.contrib import admin
from django.urls import path
from appvino import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('usuariosFormularios', views.usuariosFormulario, name='usuariosFormulario'),
    path('ingresoCorrecto', views.ingresoCorrecto, name='ingresoCorrecto'),
    path('vinosFormularios', views.vinosFormulario, name='vinosFormulario'),
    path('bodegasFormularios', views.bodegasFormulario, name='bodegasFormulario'),
    path('busquedaUsuario', views.busquedaUsuario, name='busquedaUsuario'),
    path('buscar/', views.buscar, name='buscar'),
    path('buscarVino/', views.buscarVino, name='buscarVino'),
    path('busquedaVino', views.busquedaVino, name='busquedaVino'),

]