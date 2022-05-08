from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'appvino/inicio.html')

def usuarios(request):
    return render(request, 'appvino/usuarios.html')

def vinos(request):
    return render(request, 'appvino/vinos.html')

def bodegas(request):
    return render(request, 'appvino/bodegas.html')