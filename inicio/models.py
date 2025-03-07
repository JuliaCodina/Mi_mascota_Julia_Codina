from django.db import models


# Create your models here.
class Mascota(models.Model):
    animal = models.TextField(null=True)
    nombre = models.CharField(max_length=20)
    raza = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    peso = models.CharField(max_length=2)
    sexo = models.CharField(max_length=1)
    año_nacimiento = models.CharField(max_length=4)
    enfermedades = models.CharField(null=True,max_length=20)
    medicacion1 = models.CharField(null=True,max_length=50)
    dosis1 = models.CharField(null=True,max_length=50)
    medicacion2 = models.CharField(null=True,max_length=50)
    dosis2 = models.CharField(null=True,max_length=50)
    comentarios = models.TextField(null=True, blank=True)
    fecha_creacion = models.DateField(null=True)
    
    def __str__(self):
        return f"{self.nombre} {self.animal} {self.raza} {self.comentarios} {self.color} {self.peso} {self.sexo} {self.año_nacimiento} {self.enfermedades} {self.medicacion1} {self.medicacion2} {self.dosis1} {self.dosis2}"

class InfoExtra(models.Model):
    mascota = models.OneToOneField(Mascota, on_delete=models.CASCADE)
    avatar_mascota = models.ImageField(upload_to='avatares_mascota',null=True, blank=True)