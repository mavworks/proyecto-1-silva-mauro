from django.db import models
from django.contrib.auth.models import User

class InfoUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
    
class Resenia(models.Model):
    titulo = models.CharField(max_length=20)
    subtitulo = models.CharField(max_length=20)
    contenido = models.TextField(null=True)
    autor = models.CharField(max_length=20)
    fecha_de_creacion = models.DateField(null=True)
    
    def __str__(self):
        return f'Reseña: {self.titulo}'
    
