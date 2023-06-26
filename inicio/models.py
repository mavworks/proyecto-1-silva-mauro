from django.db import models

class Producto(models.Model):
    tipo = models.CharField(max_length=20)
    precio = models.IntegerField()