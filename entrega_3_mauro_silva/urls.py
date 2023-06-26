from django.contrib import admin
from django.urls import path
from entrega_3_mauro_silva import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', views.inicio),
    path("otra/", views.otro),
    path('fecha-actual/', views.fecha)
]
