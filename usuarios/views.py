from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as django_login
from usuarios.forms import FormularioRegistro, FormularioEdicion, User
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from usuarios.models import InfoExtra, User




# Create your views here.
def login (request):
    if request.method =='POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario=formulario.get_user()
            
            django_login(request, usuario)
            
            InfoExtra.objects.get_or_create(user=usuario)
                        
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
    
    info_extra = request.user.infoextra
    
    if request.method =='POST':
        formulario = FormularioEdicion(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            
            if formulario.cleaned_data.get('avatar'):
                info_extra.avatar = formulario.cleaned_data.get('avatar')
                
            info_extra.save()
            formulario.save()
                        
            return redirect ('verperfil')
    else:
        formulario = FormularioEdicion(instance=request.user, initial={'avatar': info_extra.avatar})
    
    return render (request, 'usuarios/editarperfil.html', {'formulario':formulario})

class CambioPassword (PasswordChangeView):
    template_name = 'usuarios/cambiarpass.html'
    success_url = reverse_lazy ('inicio')
    
def verperfil (request):
    
    formulario = FormularioEdicion(request.GET, request.FILES, instance=request.user)
    if formulario.is_valid():
        
        
        Mascota_preferida_a_buscar = formulario.cleaned_data.get('Mascota_preferida') 
        user = User.objects.filter( Mascota_preferida_a_buscar__icontains=Mascota_preferida_a_buscar) 
    return render(request, 'usuarios/verperfil.html', {'formulario': formulario})