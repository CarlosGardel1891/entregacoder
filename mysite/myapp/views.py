from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Curso, Estudiante, Profesor, Entregable


# Create your views here.

def home(request):
    

    return render(request, "inicio.html")

def gCurso(request):
    cursos = Curso.objects.all()

    return render(request, "gCursos.html", {"cursos": cursos})

def registrarCurso(request):
    nombre=request.POST['txtNombre']
    codigo=request.POST['txtCodigo']

    curso=Curso.objects.create(codigo= codigo, nombre= nombre)

    return redirect('/gCurso')

def eliminarCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()

    return redirect('/gCurso')

def edicionCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, "edicionCurso.html", {"curso": curso})

def editarCurso(request):
    nombre2=request.POST['txtNombre2']
    codigo2=request.POST['txtCodigo2']

    curso = Curso.objects.get(codigo=codigo2)
    curso.delete()
    curso=Curso.objects.create(codigo= codigo2, nombre= nombre2)

    return redirect('/gCurso')     

def gEstudiante(request):

    estudiante = Estudiante.objects.all()
    return render(request, "gEstudiantes.html", {"estudiante": estudiante})

def registrarEstudiante(request):
    nombre=request.POST['txtNombre']
    apellido=request.POST['txtCodigo']
    email=request.POST['txtEmail']

    estudiante2=Estudiante.objects.create(nombre= nombre, apellido=apellido, email=email)

    return redirect('/gEstudiante')

def eliminarEstudiante(request, email):
    estudiante2 = Estudiante.objects.get(email=email)
    estudiante2.delete()

    return redirect('/gEstudiante')

def edicionEstudiante(request, email):
    estudiante = Estudiante.objects.get(email=email)
    return render(request, "edicionEstudiante.html", {"estudiante": estudiante})

def editarEstudiante(request):
    
    nombre2=request.POST['txtNombre3']
    apellido2=request.POST['txtApellido3']
    email2=request.POST['txtEmail3']


    estudiante = Estudiante.objects.get(email=email2)
    estudiante.delete()

    estudiante=Estudiante.objects.create(nombre=nombre2, apellido=apellido2, email=email2)


    return redirect('/gEstudiante')

def gProfesor(request):

    profesor = Profesor.objects.all()
    return render(request, "gProfesor.html", {"profesor": profesor})

def registrarProfesor(request):
    nombre=request.POST['txtNombre']
    apellido=request.POST['txtApellido']
    email=request.POST['txtEmail']
    profesion=request.POST['txtProfesion']

    profesor=Profesor.objects.create(nombre= nombre, apellido=apellido, email=email, profesion=profesion)

    return redirect('/gProfesor')

def eliminarProfesor(request, email):
    Profesor2 = Profesor.objects.get(email=email)
    Profesor2.delete()

    return redirect('/gProfesor')

def edicionProfesor(request, email):
    profesor = Profesor.objects.get(email=email)
    
    return render(request, "edicionProfesor.html", {"profesor": profesor})

def editarProfesor(request):
    
    nombre2=request.POST['txtNombre3']
    apellido2=request.POST['txtApellido3']
    email2=request.POST['txtEmail3']
    profesion2=request.POST['txtprofesion3']


    profesor = Profesor.objects.get(email=email2)
    profesor.delete()

    profesor2=Profesor.objects.create(nombre=nombre2, apellido=apellido2, email=email2, profesion=profesion2)


    return redirect('/gProfesor')

def gEntregable(request):

    entregable = Entregable.objects.all()
    return render(request, "gEntregable.html", {"entregable": entregable})

def registrarEntregable(request):
    nombre=request.POST['txtNombre']
    fecha=request.POST['txtFecha']

    entregable=Entregable.objects.create(nombre= nombre, fecha=fecha)

    return redirect('/gEntregable')

def eliminarEntregable(request, nombre):
    nombre2 = Entregable.objects.get(nombre=nombre)
    nombre2.delete()

    return redirect('/gEntregable')

def edicionEntregable(request, nombre):
    entregable = Entregable.objects.get(nombre=nombre)
    
    return render(request, "edicionEntregable.html", {"entregable": entregable})

def editarEntregable(request):
    
    nombre2=request.POST['txtNombre3']
    fecha2=request.POST['txtFecha3']

    entregable = Entregable.objects.get(nombre=nombre2)
    entregable.delete()

    entregable2=Entregable.objects.create(nombre=nombre2, fecha=fecha2)

    return redirect('/gEntregable')





