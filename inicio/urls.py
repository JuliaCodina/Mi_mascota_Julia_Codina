from inicio.views import inicio, crear_mascota, datos_de_mascotas
from django.urls import path

urlpatterns = [
    path('', inicio, name= 'inicio/inicio'),
    path('crearmascota/', crear_mascota, name='crear_mascota'),
    path('datosdemascotas/', datos_de_mascotas, name='datos_de_mascotas')
]