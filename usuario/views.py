from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as django_login
from usuario.form import FormularioRegistro, FormularioEditarPerfil, BuscarResenia, FormularioEditarResenia
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from usuario.models import InfoUsuario, Resenia, FotoResenia
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

def login(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data['username']
            contrasenia = formulario.cleaned_data['password']
            user = authenticate(username=usuario, password=contrasenia)
            
            django_login(request,user)
            
            InfoUsuario.objects.get_or_create(user=user)
            
            return redirect('inicio:inicio')
        else:
            return render(request, 'usuario/login.html', {'formulario':formulario})
    
    formulario = AuthenticationForm()
    return render(request, 'usuario/login.html', {'formulario':formulario})

def registro(request):
    
    if request.method == 'POST':
        formulario = FormularioRegistro(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('usuario:login')
        else:
            return render(request, 'usuario/registro.html', {'formulario':formulario}) 
    
    formulario = FormularioRegistro()
    return render(request, 'usuario/registro.html', {'formulario':formulario}) 

@login_required
def editar_perfil(request):
    info_extra_usuario = request.user.infousuario
    if request.method =='POST':
        formulario = FormularioEditarPerfil(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            avatar = formulario.cleaned_data.get('avatar')
            if avatar: 
                info_extra_usuario.avatar = avatar
                info_extra_usuario.save()
            
            formulario.save()
            return redirect('inicio:inicio')
        else:
            return render(request, 'usuario/editar_perfil.html', {'formulario':formulario})
        
    else:
        formulario = FormularioEditarPerfil(initial={'avatar': info_extra_usuario.avatar}, instance=request.user)
    
    return render(request, 'usuario/editar_perfil.html', {'formulario':formulario}) 

class CambiarPass(LoginRequiredMixin, PasswordChangeView):
    template_name = 'usuario/cambiar_pass.html'
    success_url = reverse_lazy('usuario:editar_perfil')
    

class Postear(LoginRequiredMixin, CreateView):
     model = Resenia
     template_name = 'usuario/postear.html'
     fields = ['titulo', 'subtitulo', 'contenido', 'autor', 'fecha_de_creacion']
     success_url = reverse_lazy('usuario:resenias')

def listar_resenias(request):
    
    formulario = BuscarResenia(request.GET)
    if formulario.is_valid():
        titulo_a_buscar = formulario.cleaned_data.get('titulo', '')
        resenias = Resenia.objects.filter(titulo__icontains=titulo_a_buscar)
    
    formulario = BuscarResenia()
    return render(request, 'usuario/resenias.html', {'formulario':formulario, 'resenias':resenias})
  
# class EditarResenia(LoginRequiredMixin, UpdateView):
#     model = Resenia
#     template_name = 'usuario/modificar_resenia.html'  
#     fields = ['titulo', 'subtitulo', 'contenido', 'autor', 'fecha_de_creacion']
#     success_url = reverse_lazy('usuario:listar_resenias')
    
@login_required
def editar_resenia(request):
    foto_resenia = request.resenia.fotoresenia
    if request.method =='POST':
        formulario = FormularioEditarResenia(request.POST, request.FILES, instance=request.resenia)
        if formulario.is_valid():
            img_resenias = formulario.cleaned_data.get('foto_resenias')
            if img_resenias: 
                foto_resenia.img_resenias = img_resenias
                foto_resenia.save()
            
            formulario.save()
            return redirect('inicio:inicio')
        else:
            return render(request, 'usuario/editar_resenia.html', {'formulario':formulario})
        
    else:
        formulario = FormularioEditarResenia(initial={'img_resenias': foto_resenia.img_resenias}, instance=request.resenia)
    
    return render(request, 'usuario/editar_resenia.html', {'formulario':formulario}) 
    
class EliminarResenia(LoginRequiredMixin, DeleteView): 
    model = Resenia
    template_name = 'usuario/eliminar_resenia.html'  
    success_url = reverse_lazy('usuario:resenias') 
    
class MostrarResenia(DetailView):
    model = Resenia
    template_name = 'usuario/mostrar_resenia.html'    
    
def perfil(request):
    return render(request, 'usuario/perfil.html')