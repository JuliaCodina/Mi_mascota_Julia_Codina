from inicio.views import inicio, crear_mascota, datos_de_mascotas, ver_mascotas, acercademi, agregaravatarmascota, contactenos, ModificarMascotaVista, EliminarMascotaVista
from django.urls import path
from django.conf import settings


urlpatterns = [
    path('', inicio, name= 'inicio'),
    path('crearmascota/', crear_mascota, name='crear_mascota'),
    path('datosdemascotas/', datos_de_mascotas, name='datos_de_mascotas'),
    path('vermascotas/<int:id_mascota>/', ver_mascotas, name='ver_mascotas'),
    path('contactenos/', contactenos, name='contactenos'),
    path('modificarmascotas/<int:pk>/', ModificarMascotaVista.as_view(), name='modificar_mascotas'),
    path('eliminarmascotas/<int:pk>/', EliminarMascotaVista.as_view(), name='eliminar_mascotas'),
    path('contactenos/', contactenos, name='contactenos'),
    path('acercademi/', acercademi, name='acercademi'),
    path('agregaravatarmascota/', agregaravatarmascota, name='agregaravatarmascota'),
]