from django import forms
from inicio.models import Mascota

class CrearMascota(forms.Form):
    avatar_mascota = forms.ImageField(required=False)
    animal = forms.CharField(required=False, max_length=20)
    nombre = forms.CharField(max_length=20)
    raza = forms.CharField(max_length=20)
    color = forms.CharField(max_length=20)
    peso = forms.CharField(max_length=5)
    sexo = forms.CharField(max_length=1)
    año_nacimiento = forms.CharField(max_length=4)
    enfermedades = forms.CharField(max_length=20, required=False)
    medicacion1 = forms.CharField(max_length=50, required=False)
    dosis1 = forms.CharField(max_length=50, required=False)
    medicacion2 = forms.CharField(max_length=50, required=False)
    dosis2 = forms.CharField(max_length=50, required=False)
    comentarios = forms.CharField(widget=forms.Textarea, required=False)
    fecha_creacion = forms.DateField(required=False, widget=forms.DateInput (attrs= {'type':'date'}))
    
class BuscarMascota (forms.Form):
    
    nombre = forms.CharField(max_length=20, required=False)
    raza = forms.CharField(max_length=20, required=False)
    
class ModificarMascota (forms.ModelForm):
    fecha_creacion = forms.DateField(required=False, widget=forms.DateInput (attrs= {'type':'date'}))
    class Meta:
        model= Mascota
        fields = '__all__'
   