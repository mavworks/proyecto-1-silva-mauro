from django.contrib import admin
from django.urls import path
from entrega_3_mauro_silva import views


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("crear-producto/<str:tipo>/<int:precio>/", views.crear_producto)
]
