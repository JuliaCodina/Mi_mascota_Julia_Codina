from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from inicio.models import Mascota
from inicio.forms import CrearMascota, BuscarMascota, ModificarMascota
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
def inicio(request):
     
    
    hora_actual = datetime.now()
    return render (request, 'inicio/inicio.html', {'hora':hora_actual})


def crear_mascota (request):
        
    print(request.GET)
    print(request.POST)
            
    formulario = CrearMascota()
    
        
    if request.method == "POST":
        formulario = CrearMascota(request.POST, request.FILES)
        if formulario.is_valid():
                       
            animal = formulario.cleaned_data.get('animal')          
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
            fecha_creacion = formulario.cleaned_data.get('fecha_creacion')
            

            
            mascota= Mascota(animal=animal, fecha_creacion=fecha_creacion, nombre=nombre, raza=raza, sexo=sexo, color=color, peso=peso, año_nacimiento=año_nacimiento, enfermedades=enfermedades, medicacion1=medicacion1, dosis1=dosis1, medicacion2=medicacion2, dosis2=dosis2, comentarios=comentarios)
            
            mascota.save()

            
            return redirect("datos_de_mascotas")
            
    return render (request, 'inicio/crearmascota.html', {'formulario': formulario})


def datos_de_mascotas(request):
      
    mascotas = Mascota.objects.all()
    formulario = BuscarMascota(request.GET)
    if formulario.is_valid():
        animal_a_buscar = formulario.cleaned_data.get('animal')
        nombre_a_buscar = formulario.cleaned_data.get('nombre')
        raza_a_buscar = formulario.cleaned_data.get('raza') 
        mascotas = Mascota.objects.filter(animal__icontains=animal_a_buscar, raza__icontains=raza_a_buscar, nombre__icontains=nombre_a_buscar) 
    return render(request, 'inicio/datosdemascotas.html', {'mascotas':mascotas, 'formulario': formulario})

@login_required
def ver_mascotas(request, id_mascota):

    
    mascota = Mascota.objects.get (id=id_mascota)
    return render (request, 'inicio/vermascotas.html', {'mascota':mascota}) 


#CLASES BASADAS EN VISTAS
class ModificarMascotaVista(LoginRequiredMixin, UpdateView):
    model = Mascota
    template_name= "inicio/CBV/modificarmascotas.html"
    form_class = ModificarMascota
    success_url = reverse_lazy ('datos_de_mascotas')

class EliminarMascotaVista(LoginRequiredMixin, DeleteView):
    model = Mascota
    template_name= "inicio/CBV/eliminarmascotas.html"
    success_url = reverse_lazy ('datos_de_mascotas')
    

def contactenos(request):
      
    return render (request, 'inicio/contactenos.html')

def acercademi(request):
      
    return render (request, 'inicio/acercademi.html')



    

    