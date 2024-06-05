from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import tabla9, tabla10
from .forms import tabla9Form, tabla10Form
# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')
def diario(request):
    return render(request, 'paginas/diario.html')
def ventas(request):
    return render(request, 'paginas/ventas.html')
def compras(request):
    return render(request, 'paginas/compras.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')

#TABLA 9---------------------------------------------------------------------------------------
def libro9 (request):
    libro9 = tabla9.objects.all()
    return render(request, 'tabla9/index.html', {'libro9': libro9 })

def crear9 (request):
    formulario = tabla9Form(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libro9')
    return render(request, 'tabla9/crear.html', {'formulario': formulario })

def editar9 (request, id):
    libro9 = tabla9.objects.get(id=id)
    formulario = tabla9Form(request.POST or None, request.FILES or None, instance=libro9)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libro9')
    return render(request, 'tabla9/editar.html', {'formulario': formulario})

def eliminar9(request, id):
    libro9 = tabla9.objects.get(id=id)
    libro9.delete()
    return redirect('libro9')
#FIN TABLA 9 ------------------------------------------------------------------------------------
#TABLA 10 ---------------------------------------------------------------------------------------
def libros(request):
    libros = tabla10.objects.all()
    # Ordena la lista de libros por el campo 'num'
    libros = sorted(libros, key=lambda x: x.num)
    return render(request, 'libros/index.html', {'libros': libros })

def crear_codigo(request):
    formulario = tabla10Form(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/crear.html', {'formulario': formulario})

def editar(request, id):
    libros = tabla10.objects.get(id=id)
    formulario = tabla10Form(request.POST or None, request.FILES or None, instance=libros)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/editar.html', {'formulario': formulario})

def eliminar(request, id):
    libros = tabla10.objects.get(id=id)
    libros.delete()
    return redirect('libros')

#FIN TABLA 10 -----------------------------------------------------------------------------------
