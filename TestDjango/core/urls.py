from django.urls import path
from .views import contacto, index, nosotros, servicios, inicio, registro

urlpatterns = [
    path('index', index,name="index"),
    path('contacto', contacto,name="contacto"),
    path('nosotros', nosotros,name="nosotros"),
    path('servicios', servicios,name="servicios"),
    path('inicio', inicio,name="inicio"),
    path('registro', registro,name="registro"),
]


