from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    tipoUsuario=models.CharField(max_length=20)
    edad=models.IntegerField()
    mail=models.EmailField()

    def __str__(self):
        return f"Usuario {self.nombre} {self.apellido}"
class Vinos(models.Model):
    varietal=models.CharField(max_length=30)
    bodega=models.CharField(max_length=30)
    año=models.IntegerField()
    nombre=models.CharField(max_length=50)

    def __str__(self):
        return f"Vino {self.nombre} de bodega {self.bodega}"

class Bodegas(models.Model):
    nombre=models.CharField(max_length=50)
    provincia=models.CharField(max_length=30)
    departamento=models.CharField(max_length=40)

    def __str__(self):
        return f"Bodega {self.nombre}"
