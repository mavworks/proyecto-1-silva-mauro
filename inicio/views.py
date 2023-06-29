from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from inicio.models import Persona, Dj, Pista
from inicio.form import EntrarPersonaFormulario, BuscarPersonaFormulario, QueToqueFormulario, SiTocaFormulario, AbrirPistaFormulario, BuscarPistaFormulario

def inicio(request):
    return render(request, 'inicio/inicio.html')
  
#Personas
  
def dejar_entrar_persona(request):
    
    if request.method =='POST':
        formulario = EntrarPersonaFormulario(request.POST)
        
        if formulario.is_valid():
            info = formulario.cleaned_data
            persona = Persona(nombre=info['nombre'], edad=info['edad'])
            persona.save()
            return redirect('inicio:listar personas')
        else:
            return render(request, 'inicio/listar-personas.html', {'formulario':formulario})
        
    formulario = EntrarPersonaFormulario()
    return render(request, 'inicio/dejar-entrar.html', {'formulario':formulario})

def listar_personas(request):
    formulario = BuscarPersonaFormulario(request.GET)
    if formulario.is_valid():
        nombre_a_buscar = formulario.cleaned_data['nombre']
        listado_de_personas = Persona.objects.filter(nombre__icontains=nombre_a_buscar)
         
    formulario = BuscarPersonaFormulario()
    return render(request, 'inicio/listar-personas.html', {'formulario':formulario, 'personas':listado_de_personas})

#Djs

def que_toque(request):
    
    if request.method =='POST':
        formulario = QueToqueFormulario(request.POST)
        
        if formulario.is_valid():
            info = formulario.cleaned_data
            dj = Dj(nombre=info['nombre'], canciones=info['canciones'])
            dj.save()
            return redirect('inicio:listar djs')
        
        else:
            return render(request, 'inicio/listar-djs.html', {'formulario':formulario})
        
    formulario = QueToqueFormulario()
    return render(request, 'inicio/que-toque.html', {'formulario':formulario})

def listar_djs(request):
    formulario = SiTocaFormulario(request.GET)
    if formulario.is_valid():
        nombre_a_buscar = formulario.cleaned_data['nombre']
        listado_de_djs = Dj.objects.filter(nombre__icontains=nombre_a_buscar)
         
    formulario = SiTocaFormulario()
    return render(request, 'inicio/listar-djs.html', {'formulario':formulario, 'djs':listado_de_djs})

#Pistas

def abrir_pista(request):
    
    if request.method =='POST':
        formulario = AbrirPistaFormulario(request.POST)
        
        if formulario.is_valid():
            info = formulario.cleaned_data
            pista = Pista(nombre=info['nombre'], capacidad=info['capacidad'])
            pista.save()
            return redirect('inicio:listar pistas')
        
        else:
            return render(request, 'inicio/listar-pistas.html', {'formulario':formulario})
        
    formulario = AbrirPistaFormulario()
    return render(request, 'inicio/abrir-pista.html', {'formulario':formulario})

def listar_pistas(request):
    formulario = BuscarPistaFormulario(request.GET)
    if formulario.is_valid():
        nombre_a_buscar = formulario.cleaned_data['nombre']
        listado_de_pistas = Pista.objects.filter(nombre__icontains=nombre_a_buscar)
         
    formulario = BuscarPistaFormulario()
    return render(request, 'inicio/listar-pistas.html', {'formulario':formulario, 'pistas':listado_de_pistas})

