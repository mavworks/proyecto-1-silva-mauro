from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()
    
class Dj(models.Model):
    nombre = models.CharField(max_length=20)
    canciones = models.IntegerField()
    
class Pista(models.Model):
    nombre = models.CharField(max_length=20)
    capacidad = models.IntegerField()