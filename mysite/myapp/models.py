from django.db import models

# Create your models here.

class Curso(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)

class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(primary_key=True, max_length=100)
    profesion = models.CharField(max_length=50)

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(primary_key=True, max_length=100)

class Entregable(models.Model):
    nombre = models.CharField(primary_key=True, max_length=6)
    fecha = models.CharField(max_length=50)
