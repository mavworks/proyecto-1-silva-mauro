from django.shortcuts import render
from inicio.models import Invitado, Dj
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from inicio.form import BuscarDj

def inicio(request):
    return render(request, 'inicio/inicio.html')

def about(request):
    return render(request, 'inicio/about.html')

 
class DejarEntrar(LoginRequiredMixin, CreateView):
    model = Invitado
    template_name = 'inicio/CBV/dejar_entrar_CBV.html'
    fields = ['nombre', 'edad', 'descripcion']
    success_url = reverse_lazy('inicio:listar_invitados')

class ListarInvitados(ListView, ):
    model = Invitado
    template_name = 'inicio/CBV/listar_invitados_CBV.html'  
    context_object_name = 'invitados'
    
class ModificarInvitado(LoginRequiredMixin, UpdateView):
    model = Invitado
    template_name = 'inicio/CBV/modificar_invitado_CBV.html'  
    fields = ['nombre', 'edad', 'descripcion']
    success_url = reverse_lazy('inicio:listar_invitados')
    
class SacarInvitado(LoginRequiredMixin, DeleteView):
    model = Invitado
    template_name = 'inicio/CBV/sacar_invitado_CBV.html'  
    success_url = reverse_lazy('inicio:listar_invitados') 
    
class MostrarInvitado(DetailView):
    model = Invitado
    template_name = 'inicio/CBV/mostrar_invitado_CBV.html'

 

class ContratarDj(LoginRequiredMixin, CreateView):
     model = Dj
     template_name = 'inicio/CBV/contratar_dj_CBV.html'
     fields = ['nombre', 'canciones', 'descripcion','fecha_de_presentacion']
     success_url = reverse_lazy('inicio:listar_djs')

def listar_djs(request):
    
    formulario = BuscarDj(request.GET)
    if formulario.is_valid():
        nombre_a_buscar = formulario.cleaned_data.get('nombre', '')
        djs = Dj.objects.filter(nombre__icontains=nombre_a_buscar)
    
    formulario = BuscarDj()
    return render(request, 'inicio/listar_djs.html', {'formulario':formulario, 'djs':djs})
    
    
class ModificarDj(LoginRequiredMixin, UpdateView):
    model = Dj
    template_name = 'inicio/CBV/modificar_dj_CBV.html'  
    fields = ['nombre', 'canciones', 'descripcion']
    success_url = reverse_lazy('inicio:listar_djs')
    
class DespedirDj(LoginRequiredMixin, DeleteView): 
    model = Dj
    template_name = 'inicio/CBV/despedir_dj_CBV.html'  
    success_url = reverse_lazy('inicio:listar_djs') 
    
class MostrarDj(DetailView):
    model = Dj
    template_name = 'inicio/CBV/mostrar_dj_CBV.html'    
    
