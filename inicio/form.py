from django import forms
#Persona
class EntrarInvitadoFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    edad = forms.IntegerField() 
    
class BuscarInvitadoFormulario(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)
#Djs
class QueToqueFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    canciones = forms.IntegerField() 
    
class SiTocaFormulario(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)
#Pistas
class AbrirPistaFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    capacidad = forms.IntegerField() 
    
class BuscarPistaFormulario(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)