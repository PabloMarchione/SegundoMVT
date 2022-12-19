from django.db import models

# Create your models here. class


class Jugador(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    edad=models.IntegerField()
    posicion=models.CharField(max_length=20)
    equipo=models.CharField(max_length=20)
    
    class Meta:  
        verbose_name_plural = 'Jugadores'
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Equipo(models.Model):
    nombre=models.CharField(max_length=20)
    apodo=models.CharField(max_length=20)
    titulosInternacionales=models.IntegerField(default=0)
    fundacion=models.DateField(default="1999-10-9")
    
    def __str__(self):
        return self.nombre
    

class Estadio(models.Model):
    nombre=models.CharField(max_length=20)
    apodo=models.CharField(max_length=20)
    fundacion=models.DateField(default="1999-10-9")
    def __str__(self):
        return self.nombre
