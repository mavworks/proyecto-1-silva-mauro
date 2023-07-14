from django.urls import path
from usuario import views
from django.contrib.auth.views import LogoutView
app_name = 'usuario'

urlpatterns = [
    path('login/',views.login, name='login'),
    path('registro/', views.registro, name='registro'),
    path('logout/', LogoutView.as_view(template_name='usuario/logout.html'), name='logout'),
    path('perfil/editar/', views.editar_perfil, name = 'editar_perfil'),
    path('perfil/editar/pass', views.CambiarPass.as_view(), name = 'cambiar_pass'),
    path('resenias', views.listar_resenias, name = 'resenias'),
    path('resenias/postear', views.Postear.as_view(), name = 'postear'),
    path('resenias/editar_resenia', views.editar_resenia, name = 'editar_resenia'),
    path('resenias/eliminar_resenia', views.EliminarResenia.as_view(), name = 'eliminar_resenia'),
    path('resenias/mostrar', views.MostrarResenia.as_view(), name = 'mostrar_resenia'),


    
]
  