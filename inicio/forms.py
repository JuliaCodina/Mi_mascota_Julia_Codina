from django import forms

class CrearMascota(forms.Form):
    nombre = forms.CharField(max_length=20)
    raza = forms.CharField(max_length=20)
    color = forms.CharField(max_length=20)
    peso = forms.CharField(max_length=2)
    sexo = forms.CharField(max_length=1)
    año_nacimiento = forms.CharField(max_length=4)
    enfermedades = forms.CharField(max_length=20)
    medicacion1 = forms.CharField(max_length=50)
    dosis1 = forms.CharField(max_length=50)
    medicacion2 = forms.CharField(max_length=50)
    dosis2 = forms.CharField(max_length=50)
    comentarios = forms.CharField(widget=forms.Textarea, required=False)
    
class BuscarMascota (forms.Form):
    nombre = forms.CharField(max_length=20, required=False)
    enfermedades = forms.CharField(max_length=20, required=False)
    medicacion1 = forms.CharField(max_length=50, required=False)
    medicacion2 = forms.CharField(max_length=50, required=False)
   