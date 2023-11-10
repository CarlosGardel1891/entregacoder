from django.shortcuts import render, redirect
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

    return render(request, "edicionCurso.html", {"curso":curso})

def editarCurso(request):
    nombre=request.POST['txtNombre2']
    codigo=request.POST['txtCodigo2']
    
    cursoo = Curso.objects.get(codigo=codigo)
    
    cursoo.nombre = nombre
    cursoo.codigo = codigo
    
    cursoo.save

    return redirect('/')


