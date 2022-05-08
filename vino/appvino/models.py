from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    tipoUsuario=models.CharField(max_length=20)
    edad=models.IntegerField()
    mail=models.EmailField()

    def __str__(self):
        return "Usuarios"
class Vinos(models.Model):
    varietal=models.CharField(max_length=30)
    bodega=models.CharField(max_length=30)
    año=models.IntegerField()
    nombre=models.CharField(max_length=50)

    def __str__(self):
        return "Vinos"

class Bodegas(models.Model):
    nombre=models.CharField(max_length=50)
    provincia=models.CharField(max_length=30)
    departamento=models.CharField(max_length=40)

    def __str__(self):
        return "Bodegas"
