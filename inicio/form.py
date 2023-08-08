from django import forms
from ckeditor.fields import RichTextField


class BuscarDj(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)
    
# class ContratarFormulario(forms.Form):
#     nombre = forms.CharField(max_length=20)
#     canciones = forms.IntegerField()
#     descripcion = RichTextField()
#     fecha_de_presentacion = forms.DateField(required=False)
#     imagen_dj = forms.ImageField(required=False)

# class EditarDjFormulario(forms.Form):
#     nombre = forms.CharField(max_length=20)
#     canciones = forms.IntegerField()
#     descripcion = RichTextField()
#     fecha_de_presentacion = forms.DateField(required=False)
#     imagen_dj = forms.ImageField(required=False)
    