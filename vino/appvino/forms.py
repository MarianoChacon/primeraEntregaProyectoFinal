from django import forms



class UsuarioFormulario(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    tipoUsuario=forms.CharField(max_length=20)
    edad=forms.IntegerField()
    mail=forms.EmailField()

class VinosFormulario(forms.Form):
    varietal=forms.CharField(max_length=30)
    bodega=forms.CharField(max_length=30)
    año=forms.IntegerField()
    nombre=forms.CharField(max_length=50)

class BodegasFormulario(forms.Form):
    nombre=forms.CharField(max_length=50)
    provincia=forms.CharField(max_length=30)
    departamento=forms.CharField(max_length=40)