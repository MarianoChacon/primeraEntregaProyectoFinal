from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from appvino.models import *
# Create your views here.
def inicio(request):
    return render(request, 'appvino/inicio.html')

def usuarios(request):
    return render(request, 'appvino/usuarios.html')

def vinos(request):
    return render(request, 'appvino/vinos.html')

def bodegas(request):
    return render(request, 'appvino/bodegas.html')

def usuariosFormulario(request):
    if request.method == 'POST':
        miFormulario=UsuarioFormulario(request.POST)

        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data #esto me extrae la info que ingresó por POST
            usuario=Usuarios(nombre=informacion['nombre'],apellido=informacion['apellido'],tipoUsuario=informacion['tipoUsuario'],edad=informacion['edad'],mail=informacion['mail'])
            usuario.save()
            return render(request, 'appvino/inicio.html')
    
    else:
        miFormulario=UsuarioFormulario()
    
    return render (request, 'appvino/usuariosFormulario.html', {'formulario':miFormulario})