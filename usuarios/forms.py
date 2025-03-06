from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User
#from usuarios.views import login, registro

class FormularioRegistro (UserCreationForm):
   
        username = forms.CharField (label='Usuario')
        email = forms.EmailField()
        password1 = forms.CharField (label='Contraseña', widget=forms.PasswordInput)
        password2 = forms.CharField (label='Repetir Contraseña', widget=forms.PasswordInput)
        
        class Meta:
            model = User
            exclude = ['last_login', 'groups', 'user_permissions','first_name', 'last_name','date_joined', 'username_validator', 'is_staff', 'is_active', 'password', 'is_superuser']
            


class FormularioEdicion (UserChangeForm):
        password = None

        
        class Meta:
            model = User
            exclude = ['password','username','last_login', 'groups', 'user_permissions','date_joined', 'username_validator', 'is_staff', 'is_active', 'password1','password2', 'is_superuser']
            