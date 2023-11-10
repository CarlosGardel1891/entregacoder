from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Curso

# Create your views here.

def home(request):
    cursos = Curso.objects.all()

    return render(request, "gCursos.html", {"cursos": cursos})

def registrarCurso(request):
    nombre=request.POST['txtNombre']
    codigo=request.POST['txtCodigo']

    curso=Curso.objects.create(codigo= codigo, nombre= nombre)

    return redirect('/')

def eliminarCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()

    return redirect('/')

def edicionCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, "edicionCurso.html", {"curso": curso})

def editarCurso(request):
    nombre2=request.POST['txtNombre2']
    codigo2=request.POST['txtCodigo2']

    curso = Curso.objects.get(codigo=codigo2)
    curso.delete()
    curso=Curso.objects.create(codigo= codigo2, nombre= nombre2)

    return redirect('/')


