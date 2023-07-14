from django.urls import path
from inicio import views

app_name = 'inicio'
urlpatterns = [
    path('', views.inicio, name = 'inicio') ,
    path('about/', views.about, name = 'about'),
    
    #personas
    
    path("invitados/dejar_entrar", views.DejarEntrar.as_view(), name='dejar_entrar_invitado'),
    path('invitados', views.ListarInvitados.as_view(), name='listar_invitados'),
    path('invitados/sacar/<int:pk>', views.SacarInvitado.as_view(), name='sacar_invitado'),
    path('invitados/modificar_invitado/<int:pk>', views.ModificarInvitado.as_view(), name='mod_invitado'),
    path('invitados/mostrar_invitado/<int:pk>', views.MostrarInvitado.as_view(), name='mostrar_invitado'),

    #djs 
    path("djs/contratar_dj", views.ContratarDj.as_view(), name='contratar_dj'),
    # path('djs', views.ListarDjs.as_view(), name='listar_djs'),
    # path('djs/contratar_dj', views.contratar_dj, name ='contratar_dj'),
    path('djs', views.listar_djs, name='listar_djs'),
    path("djs/despedir/<int:pk>", views.DespedirDj.as_view(), name='despedir_dj'),
    path("djs/modificar_dj/<int:pk>", views.ModificarDj.as_view(), name='mod_dj'),
    path('djs/mostrar_dj/<int:pk>', views.MostrarDj.as_view(), name='mostrar_dj'),
]