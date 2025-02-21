from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from inicio.models import Mascota
from inicio.forms import CrearMascota
from inicio.forms import BuscarMascota

# Create your views here.
def inicio(request):
    #return HttpResponse("<h1>vista<h1>")
    hora_actual = datetime.now()
    return render (request, 'inicio/inicio.html', {'hora':hora_actual})

def crear_mascota(request):
    
    print(request.GET)
    print(request.POST)
    
    formulario = CrearMascota()
    
    if request.method == "POST":
        formulario = CrearMascota(request.POST)
        if formulario.is_valid():
            
            nombre = formulario.cleaned_data.get('nombre')
            raza = formulario.cleaned_data.get('raza')
            color = formulario.cleaned_data.get('color')
            peso = formulario.cleaned_data.get('peso')
            sexo = formulario.cleaned_data.get('sexo')
            año_nacimiento = formulario.cleaned_data.get('año_nacimiento')
            enfermedades = formulario.cleaned_data.get('enfermedades')
            medicacion1 = formulario.cleaned_data.get('medicacion1')
            dosis1 = formulario.cleaned_data.get('dosis1')
            medicacion2 = formulario.cleaned_data.get('medicacion2')
            dosis2 = formulario.cleaned_data.get('dosis2')
            comentarios = formulario.cleaned_data.get('comentarios')
            
          
            mascota= Mascota(nombre=nombre, raza=raza, sexo=sexo, color=color, peso=peso, año_nacimiento=año_nacimiento, enfermedades=enfermedades, medicacion1=medicacion1, dosis1=dosis1, medicacion2=medicacion2, dosis2=dosis2, comentarios=comentarios)
            mascota.save()
            
            return redirect("datos_de_mascotas")
            
    return render (request, 'crearmascota.html', {'formulario': formulario})

def datos_de_mascotas(request):
      
    mascotas = Mascota.objects.all()
    formulario = BuscarMascota(request.GET)
    if formulario.is_valid():
        nombre_a_buscar = formulario.cleaned_data.get('nombre')
        enfermedades_a_buscar = formulario.cleaned_data.get('enfermedades')
        medicacion1_a_buscar = formulario.cleaned_data.get('medicacion1')
        medicacion2_a_buscar = formulario.cleaned_data.get('medicacion2')
        mascotas = Mascota.objects.filter(nombre__icontains=nombre_a_buscar, enfermedades__icontains=enfermedades_a_buscar, medicacion1__icontains=medicacion1_a_buscar, medicacion2__icontains=medicacion2_a_buscar)
        
    return render(request, 'datosdemascotas.html', {'mascotas':mascotas, 'formulario': formulario})