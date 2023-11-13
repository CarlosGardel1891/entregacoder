from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),

    path('gCurso/', views.gCurso),
    path('registrarCurso/', views.registrarCurso),
    path('gCurso/eliminarCurso/<codigo>', views.eliminarCurso),
    path('gCurso/edicionCurso/<codigo>', views.edicionCurso),
    path('editarCurso/', views.editarCurso),

    path('gEstudiante/', views.gEstudiante),
    path('registrarEstudiante/', views.registrarEstudiante),
    path('gEstudiante/eliminarEstudiante/<email>', views.eliminarEstudiante),
    path('gEstudiante/edicionEstudiante/<email>', views.edicionEstudiante),
    path('editarEstudiante/', views.editarEstudiante),

    path('gProfesor/', views.gProfesor),
    path('registrarProfesor/', views.registrarProfesor),
    path('gProfesor/eliminarProfesor/<email>', views.eliminarProfesor),
    path('gProfesor/edicionProfesor/<email>', views.edicionProfesor),
    path('editarProfesor/', views.editarProfesor),

    path('gEntregable/', views.gEntregable),
    path('registrarEntregable/', views.registrarEntregable),
    path('gEntregable/eliminarEntregable/<nombre>', views.eliminarEntregable),
    path('gEntregable/edicionEntregable/<nombre>', views.edicionEntregable),
    path('editarEntregable/', views.editarEntregable),

]
