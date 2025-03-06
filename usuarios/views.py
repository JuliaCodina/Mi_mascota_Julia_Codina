from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as django_login
from usuarios.forms import FormularioRegistro, FormularioEdicion
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy



# Create your views here.
def login (request):
    if request.method =='POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario=formulario.get_user()
            
            django_login(request, usuario)
                        
            return redirect ('inicio')
    else:
        formulario = AuthenticationForm()
    
    return render (request, 'usuarios/login.html', {'formulario':formulario})

def registro (request):
    if request.method =='POST':
        formulario = FormularioRegistro(request.POST)
        if formulario.is_valid():
            formulario.save()
                        
            return redirect ('login')
    else:
        formulario = FormularioRegistro()
    
    return render (request, 'usuarios/registro.html', {'formulario':formulario})

def editarperfil (request):
    if request.method =='POST':
        formulario = FormularioEdicion(request.POST)
        if formulario.is_valid():
            formulario.save()
                        
            return redirect ('inicio')
    else:
        formulario = FormularioEdicion()
    
    return render (request, 'usuarios/editarperfil.html', {'formulario':formulario})

class CambioPassword (PasswordChangeView):
    template_name = 'usuarios/cambiarpass.html'
    success_url = reverse_lazy ('inicio')