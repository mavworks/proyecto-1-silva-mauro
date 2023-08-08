from django.db import models
from ckeditor.fields import RichTextField

class Invitado(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()
    descripcion = RichTextField(blank=True, null=True)
    imagen_invitado = models.ImageField(blank=True, null=True, upload_to='img_invitados')
    
    def __str__(self):
        return f'Invitado: {self.nombre} - Edad: {self.edad}'
    
class Dj(models.Model):
    nombre = models.CharField(max_length=20)
    canciones = models.IntegerField()
    descripcion = RichTextField(blank=True, null=True)
    fecha_de_presentacion = models.DateField(blank=True,null=True)
    imagen_dj = models.ImageField(blank=True, null=True, upload_to='img_djs')

    
    def __str__(self):
        return f'Dj: {self.nombre} - Canciones: {self.canciones}'