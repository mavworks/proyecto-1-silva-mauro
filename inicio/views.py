from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from inicio.models import Invitado, Dj, Pista
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

def inicio(request):
    return render(request, 'inicio/inicio.html')

def about(request):
    return render(request, 'inicio/about.html')
#Invitados
 
class DejarEntrar(LoginRequiredMixin, CreateView):
    model = Invitado
    template_name = 'inicio/CBV/dejar-entrar-CBV.html'
    fields = ['nombre', 'edad', 'descripcion']
    success_url = reverse_lazy('inicio:listar invitados')

class ListarInvitados(ListView, ):
    model = Invitado
    template_name = 'inicio/CBV/listar-invitados-CBV.html'  
    context_object_name = 'invitados'
    
class ModificarInvitado(LoginRequiredMixin, UpdateView):
    model = Invitado
    template_name = 'inicio/CBV/modificar-invitado-CBV.html'  
    fields = ['nombre', 'edad', 'descripcion']
    success_url = reverse_lazy('inicio:listar invitados')
    
class SacarInvitado(LoginRequiredMixin, DeleteView):
    model = Invitado
    template_name = 'inicio/CBV/sacar-invitado-CBV.html'  
    success_url = reverse_lazy('inicio:listar invitados') 
    
class MostrarInvitado(DetailView):
    model = Invitado
    template_name = 'inicio/CBV/mostrar-invitado-CBV.html'

 
#Djs
class ContratarDj(LoginRequiredMixin, CreateView):
    model = Dj
    template_name = 'inicio/CBV/contratar-dj-CBV.html'
    fields = ['nombre', 'canciones', 'descripcion']
    success_url = reverse_lazy('inicio:listar djs')
    
class ListarDjs(ListView):
    model = Dj
    template_name = 'inicio/CBV/listar-djs-CBV.html'  
    context_object_name = 'djs'
    
class ModificarDj(LoginRequiredMixin, UpdateView):
    model = Dj
    template_name = 'inicio/CBV/modificar-dj-CBV.html'  
    fields = ['nombre', 'canciones', 'descripcion']
    success_url = reverse_lazy('inicio:listar djs')
    
class DespedirDj(LoginRequiredMixin, DeleteView):
    model = Dj
    template_name = 'inicio/CBV/despedir-dj-CBV.html'  
    success_url = reverse_lazy('inicio:listar djs') 
    
class MostrarDj(DetailView):
    model = Dj
    template_name = 'inicio/CBV/mostrar-dj-CBV.html'    
    
#Pistas
class AbrirPista(LoginRequiredMixin, CreateView):
    model = Pista
    template_name = 'inicio/CBV/abrir-pista-CBV.html'
    fields = ['nombre', 'capacidad', 'descripcion']
    success_url = reverse_lazy('inicio:listar pistas')
    
class ListarPistas(ListView):
    model = Pista
    template_name = 'inicio/CBV/listar-pistas-CBV.html'  
    context_object_name = 'pistas'
    
class ModificarPista(LoginRequiredMixin, UpdateView):
    model = Pista
    template_name = 'inicio/CBV/modificar-pista-CBV.html'  
    fields = ['nombre', 'capacidad', 'descripcion']
    success_url = reverse_lazy('inicio:listar pistas')
    
class CerrarPista(LoginRequiredMixin, DeleteView):
    model = Pista
    template_name = 'inicio/CBV/cerrar-pista-CBV.html'  
    success_url = reverse_lazy('inicio:listar pistas') 

class MostrarPista(DetailView):
    model = Pista
    template_name = 'inicio/CBV/mostrar-pista-CBV.html'    
    