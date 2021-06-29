from django.db import models

class contacto(models.Model):
    idContacto = models.IntegerField(primary_key=True, verbose_name='ID de Contacto')
    Nombre = models.CharField(max_length=50, blank= False, null= False)
    Correo = models.CharField(max_length=254, blank= False, null= False)
    Asunto = models.CharField( max_length=50, blank= False, null= False)
    Mensaje = models.TextField( blank= False, null= False)

    def __str__(self):
         return self.Nombre



class registro(models.Model):
    idRegistro = models.IntegerField(primary_key=True, verbose_name='ID de registro')
    Usuario = models.CharField(max_length=50, verbose_name='Usuario', blank= False, null= False)
    Nombre = models.CharField(max_length=50, verbose_name='Nombre', blank= False, null= False)
    Contraseña  = models.CharField(max_length= 20, blank= False, null= False, verbose_name='Contraseña')
    Correo = models.EmailField(max_length=254, verbose_name='Correo del usuario', blank= False, null= False)
    Numero = models.IntegerField(null=False, blank=False, unique=True, verbose_name='Numero de telefono')

    def __str__(self):
        return self.Usuario