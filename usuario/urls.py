from django.urls import path
from usuario import views
from django.contrib.auth.views import LogoutView
app_name = 'usuario'

urlpatterns = [
    path('login/',views.login, name='login'),
    path('registro/', views.registro, name='registro'),
    path('logout/', LogoutView.as_view(template_name='usuario/logout.html'), name='logout'),
]
  