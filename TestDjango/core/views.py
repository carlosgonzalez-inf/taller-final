from django.shortcuts import render
from .models import contacto
from .forms import ContactoForm, RegistroForm

def contacto(request):

      datos = {
            'form': ContactoForm()

      }
    
      if request.method== 'POST':
            
            formulario = ContactoForm(request.POST)
            if formulario.is_valid:
                  formulario.save()
                  datos['mensaje']="Enviado correctamente"
                  
      return render(request, 'core/contacto.html', datos)


def index(request):
      return render(request, 'core/index.html')


def nosotros(request):
      return render(request, 'core/nosotros.html')

def servicios(request):
      return render(request, 'core/servicios.html')

def inicio(request):
      return render(request, 'core/inicio.html')

def registro(request):

      datoR = {
            'form': RegistroForm()

      }
    
      if request.method== 'POST':
            
            formulario = RegistroForm(request.POST)
            if formulario.is_valid:
                  formulario.save()
                  datos['mensaje']="Se a registrado correctamente"

      return render(request, 'core/registro.html', datoR)