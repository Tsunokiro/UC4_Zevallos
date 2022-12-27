from django.shortcuts import render
from miapp.models import Curso

# Create your views here.
def layout(request):
    return render(request, "layout.html")

def crear(request):
    return render (request,'crear_curso.html')

def crear_curso(request):
   if request.method == 'POST':
    nombre= request.POST ['nombre']
    
    curso= Curso(
        nombre=nombre
    )
    articulo.save()
    return render(request,'cursos.html')

def listar_cursos(request):
    cursos= Curso.objects.all()
    return render(request,'listar_cursos.html',{
        'titulo':'Lista de Cursos',
        'cursos': cursos
    })

def eliminar(request,id):
    cursos=Curso.objects.get(pk=id)
    cursos.delete()
    return render(request,'cursos.html')