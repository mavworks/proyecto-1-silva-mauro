from django.urls import path
from inicio import views

app_name = 'inicio'
urlpatterns = [
    path('', views.inicio, name = 'inicio') ,
    #personas
    path("invitados/dejar-entrar", views.dejar_entrar_invitado, name='dejar entrar invitado'),
    path('invitados/sacar/<int:invitado_id>', views.sacar_invitado, name='sacar invitado'),
    path('invitados/modificar-invitado/<int:invitado_id>', views.modificar_invitado, name='mod invitado'),
    path('invitados', views.listar_invitados, name='listar invitados'),
    #djs
    path("djs/que-toque", views.que_toque, name='que toque'),
    path("djs/despedir/<int:dj_id>", views.despedir, name='despedir dj'),
    path("djs/modificar-dj/<int:dj_id>", views.modificar_dj, name='mod dj'),

    path('djs', views.listar_djs, name='listar djs'),
    #pistas
    path("pistas/abrir-pista", views.abrir_pista, name='abrir pista'),
    path("pistas/cerrar-pista/<int:pista_id>", views.cerrar_pista, name='cerrar pista'),
    path("pistas/modificar-pista/<int:pista_id>", views.modificar_pista, name='mod pista'),
    path('pistas', views.listar_pistas, name='listar pistas'),
    
]