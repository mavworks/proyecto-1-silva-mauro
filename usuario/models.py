from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class InfoUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
    cumpleanios = models.DateField(blank=True, null=True)
    
class Resenia(models.Model):
    titulo = models.CharField(max_length=20)
    subtitulo = models.CharField(max_length=20)
    contenido = RichTextField(null=True, blank=True)
    autor = models.CharField(max_length=20)
    fecha_de_creacion = models.DateField(null=True)
    
    def __str__(self):
        return f'Reseña: {self.titulo}'
    