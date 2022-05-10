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

def ingresoCorrecto(request):
    return render(request, 'appvino/ingresoCorrecto.html')

def usuariosFormulario(request):
    if request.method == 'POST':
        miFormulario=UsuarioFormulario(request.POST)

        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data #esto me extrae la info que ingresó por POST
            usuario=Usuarios(nombre=informacion['nombre'],apellido=informacion['apellido'],tipoUsuario=informacion['tipoUsuario'],edad=informacion['edad'],mail=informacion['mail'])
            usuario.save()
            return render(request, 'appvino/ingresoCorrecto.html')
    
    else:
        miFormulario=UsuarioFormulario()
    
    return render (request, 'appvino/usuariosFormulario.html', {'formulario':miFormulario})

def vinosFormulario(request):
    if request.method == 'POST':
        miFormularioVino=VinosFormulario(request.POST)

        if miFormularioVino.is_valid():
            informacionVino=miFormularioVino.cleaned_data #esto me extrae la info que ingresó por POST
            vino=Vinos(varietal=informacionVino['varietal'],año=informacionVino['año'],bodega=informacionVino['bodega'],nombre=informacionVino['nombre'])
            vino.save()
            return render(request, 'appvino/ingresoCorrecto.html')
    
    else:
        miFormularioVino=VinosFormulario()
    
    return render (request, 'appvino/vinosFormulario.html', {'formulario':miFormularioVino})

def bodegasFormulario(request):
    if request.method == 'POST':
        miFormularioBod=BodegasFormulario(request.POST)

        if miFormularioBod.is_valid():
            informacionBod=miFormularioBod.cleaned_data #esto me extrae la info que ingresó por POST
            bodega=Bodegas(nombre=informacionBod['nombre'],provincia=informacionBod['provincia'],departamento=informacionBod['departamento'])
            bodega.save()
            return render(request, 'appvino/ingresoCorrecto.html')
    
    else:
        miFormularioBod=BodegasFormulario()
    
    return render (request, 'appvino/bodegasFormulario.html', {'formulario':miFormularioBod})