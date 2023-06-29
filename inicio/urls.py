from django.urls import path
from inicio import views

app_name = 'inicio'
urlpatterns = [
    path('', views.inicio, name = 'inicio') ,
    path("personas/dejar-entrar", views.dejar_entrar_persona, name='dejar entrar persona'),
    path('personas', views.listar_personas, name='listar personas'),
    path("djs/que-toque", views.que_toque, name='que toque'),
    path('djs', views.listar_djs, name='listar djs'),
    path("pistas/abrir-pista", views.abrir_pista, name='abrir pista'),
    path('pistas', views.listar_pistas, name='listar pistas'),
]