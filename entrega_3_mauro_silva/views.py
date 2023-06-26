from django.http import HttpResponse
from datetime import datetime
from django.template import loader
from inicio.models import Producto


def crear_producto(request, tipo, precio):
    template = loader.get_template("crear-producto.html")
    producto = Producto(tipo=tipo, precio=precio)
    producto.save()
    diccionario = {
        "producto" : producto,
    }
    
    renderizar_template = template.render(diccionario)
    
    return HttpResponse(renderizar_template)