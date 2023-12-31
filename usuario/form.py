from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User




class FormularioRegistro(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: '' for k in fields}


class FormularioEditarPerfil(UserChangeForm):
    password = None
    email = forms.EmailField()
    first_name = forms.CharField(label='Nombre', max_length=20)
    last_name = forms.CharField(label='Apellido', max_length=20)
    cumpleanios= forms.DateField(required=False)
    avatar = forms.ImageField(required=False)
    
    
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'cumpleanios']
        

class BuscarResenia(forms.Form):
    titulo = forms.CharField(max_length=20, required=False)

