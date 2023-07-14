from django import forms

class ContratarFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    canciones = forms.IntegerField()
    fecha_de_presentacion = forms.DateField(required=False, widget=forms.DateInput(format='%d/%m/%Y'), input_formats=('%d/%m/%Y', ))
    
class BuscarDj(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)
