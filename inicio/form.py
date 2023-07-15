from django import forms


class BuscarDj(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)
