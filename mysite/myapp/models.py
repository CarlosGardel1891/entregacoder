from django.db import models

# Create your models here.

class Curso(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)

    def cambiar_Nombre(request, nom):
        nombre=nom
    
    def cambiar_Codigo(request, cod):
        codigo=cod