from django.http import HttpResponse
from datetime import datetime
from django.template import loader


def inicio(request):
    template = loader.get_template("inicio.html")
    
    segundos = datetime.now().second
    
    diccionario = {
        'mensaje': 'bb',
        "segundos": segundos,
        "segundo_par": segundos%2 == 0,
        "no_segundos": "Impar"
    }
    
    renderizar_template = template.render(diccionario)
    
    return HttpResponse(renderizar_template)


def otro(request):
    return HttpResponse("<h1>Otra Página</h1>")

def fecha(request):
    
    fecha = datetime.now()
    
    return HttpResponse(f'fecha actual: {fecha}')