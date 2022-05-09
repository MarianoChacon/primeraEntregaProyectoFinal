from django import forms



class UsuarioFormulario(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    tipoUsuario=forms.CharField(max_length=20)
    edad=forms.IntegerField()
    mail=forms.EmailField()