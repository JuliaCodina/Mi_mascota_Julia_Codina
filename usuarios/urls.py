from django.urls import path
from usuarios.views import login, registro, editarperfil, CambioPassword, verperfil
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('usuarios/login/', login, name='login'),
    path('usuarios/logout/', LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
    path('usuarios/registro/', registro, name='registro'),
    path('usuarios/editarperfil/', editarperfil, name='editarperfil'),
    path('editarperfil/cambiarpass', CambioPassword.as_view(), name='cambiarpass'),
    path('usuarios/verperfil/', verperfil, name='verperfil'),
]