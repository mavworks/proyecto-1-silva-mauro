from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from usuario.models import Resenia, FotoResenia



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
    avatar = forms.ImageField(required=False)
    
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
        
class BuscarResenia(forms.Form):
    titulo = forms.CharField(max_length=20, required=False)
    
    
class FormularioEditarResenia(forms.ModelForm):
    class Meta:
        model = Resenia
        fields = ['titulo', 'subtitulo', 'contenido', 'autor', 'fecha_de_creacion']
        widgets = {
            'fecha_de_creacion': forms.DateInput(format='%d/%m/%Y'),
        }

class FormularioEditarFotoResenia(forms.ModelForm):
    class Meta:
        model = FotoResenia
        fields = ['foto_resenia']
    
# class FormularioEditarResenia(UserChangeForm):
#     titulo = forms.CharField(label='Titulo', max_length=20)
#     subtitulo = forms.CharField(label='Subtitulo', max_length=20)
#     contenido = forms.CharField(label='Contenido', max_length=3000)
#     autor = forms.CharField(label='autor', max_length=20)
#     fecha_de_creacion = forms.DateField(required=False, widget=forms.DateInput(format='%d/%m/%Y'), input_formats=('%d/%m/%Y', ))
#     avatar = forms.ImageField(required=False)
    
    
    # class Meta:
    #     model = Rese
    #     fields = ['email', 'first_name', 'last_name']
