from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def inicio(request):
    #return HttpResponse("<h1>vista<h1>")

    return render (request, 'inicio/inicio.html')

def saludo(request, nombre):
    hora_actual = datetime.now()
    return render (request, 'inicio/saludo.html', {'hora':hora_actual, 'nombre':nombre})