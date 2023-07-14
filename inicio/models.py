from django.db import models

class Invitado(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()
    descripcion = models.TextField(null=True)
    
    def __str__(self):
        return f'Invitado: {self.nombre} - Edad: {self.edad}'
    
class Dj(models.Model):
    nombre = models.CharField(max_length=20)
    canciones = models.IntegerField()
    descripcion = models.TextField(null=True)

    
    def __str__(self):
        return f'Dj: {self.nombre} - Canciones: {self.canciones}'
    
class Pista(models.Model):
    nombre = models.CharField(max_length=20)
    capacidad = models.IntegerField()
    descripcion = models.TextField(null=True)

    
    def __str__(self):
        return f'Pista: {self.nombre} - Capacidad: {self.capacidad}'
    
