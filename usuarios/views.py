from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as django_login
from django.contrib.auth.forms import UserCreationForm
from usuarios.forms import FormularioRegistro

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
        formulario = FormularioRegistro(request.post)
        if formulario.is_valid():
            formulario.save()
                        
            return redirect ('login')
    else:
        formulario = FormularioRegistro()
    
    return render (request, 'usuarios/registro.html', {'formulario':formulario})
