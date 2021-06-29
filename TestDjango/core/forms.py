from django import forms
from django.forms import ModelForm
from .models import contacto, registro
    
class ContactoForm(ModelForm):

    class Meta:
        model = contacto
        fields = ['Nombre','Correo','Asunto','Mensaje']


class RegistroForm(ModelForm):

    class Meta:
        model = registro
        fields = ['Usuario','Nombre','Contraseña','Correo','Numero']