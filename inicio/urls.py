from django.urls import path
from inicio import views

app_name = 'inicio'
urlpatterns = [
    path('', views.inicio, name = 'inicio') ,
    path('about/', views.about, name = 'about'),
    
    #personas
    
    path("invitados/dejar-entrar", views.DejarEntrar.as_view(), name='dejar entrar invitado'),
    path('invitados', views.ListarInvitados.as_view(), name='listar invitados'),
    path('invitados/sacar/<int:pk>', views.SacarInvitado.as_view(), name='sacar invitado'),
    path('invitados/modificar-invitado/<int:pk>', views.ModificarInvitado.as_view(), name='mod invitado'),
    path('invitados/mostrar-invitado/<int:pk>', views.MostrarInvitado.as_view(), name='mostrar invitado'),

    #djs 
    path("djs/contratar-dj", views.ContratarDj.as_view(), name='contratar dj'),
    path('djs', views.ListarDjs.as_view(), name='listar djs'),
    path("djs/despedir/<int:pk>", views.DespedirDj.as_view(), name='despedir dj'),
    path("djs/modificar-dj/<int:pk>", views.ModificarDj.as_view(), name='mod dj'),
    path('djs/mostrar-dj/<int:pk>', views.MostrarDj.as_view(), name='mostrar dj'),
    
    #pistas
    path("pistas/abrir-pista", views.AbrirPista.as_view(), name='abrir pista'),
    path('pistas', views.ListarPistas.as_view(), name='listar pistas'),
    path("pistas/cerrar-pista/<int:pk>", views.CerrarPista.as_view(), name='cerrar pista'),
    path("pistas/modificar-pista/<int:pk>", views.ModificarPista.as_view(), name='mod pista'),
    path('pistas/mostrar-pista/<int:pk>', views.MostrarPista.as_view(), name='mostrar pista'),
    
]