from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from inicio.models import Invitado, Dj, Pista
from inicio.form import EntrarInvitadoFormulario, BuscarInvitadoFormulario, QueToqueFormulario, SiTocaFormulario, AbrirPistaFormulario, BuscarPistaFormulario

def inicio(request):
    return render(request, 'inicio/inicio.html')
  
#Invitados
  
def dejar_entrar_invitado(request):
    
    if request.method =='POST':
        formulario = EntrarInvitadoFormulario(request.POST)
        
        if formulario.is_valid():
            info = formulario.cleaned_data
            invitado = Invitado(nombre=info['nombre'], edad=info['edad'])
            invitado.save()
            return redirect('inicio:listar invitados')
        else:
            return render(request, 'inicio/listar-invitados.html', {'formulario':formulario})
        
    formulario = EntrarInvitadoFormulario()
    return render(request, 'inicio/dejar-entrar.html', {'formulario':formulario})

def listar_invitados(request):
    formulario = BuscarInvitadoFormulario(request.GET)
    if formulario.is_valid():
        nombre_a_buscar = formulario.cleaned_data['nombre']
        listado_de_invitados = Invitado.objects.filter(nombre__icontains=nombre_a_buscar)
         
    formulario = BuscarInvitadoFormulario()
    return render(request, 'inicio/listar-invitados.html', {'formulario':formulario, 'invitados':listado_de_invitados})

def sacar_invitado(request, invitado_id):
    invitado = Invitado.objects.get(id=invitado_id)
    invitado.delete()
    return redirect('inicio:listar invitados')

def modificar_invitado(request):
    return render()

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

def despedir(request, dj_id):
    dj = Dj.objects.get(id=dj_id)
    dj.delete()
    return redirect('inicio:listar djs')

def modificar_dj(request):
    return render()

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

def cerrar_pista(request, pista_id):
    pista = Pista.objects.get(id=pista_id)
    pista.delete()
    return redirect('inicio:listar pistas')

def modificar_pista(request):
    return render()