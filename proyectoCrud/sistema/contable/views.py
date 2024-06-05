from django.shortcuts import render, redirect
from .models import tabla9, tabla10
from .forms import tabla9Form, tabla10Form
# Create your views here.
#PAGINAS DEL SITIO---------------------------------------------------------------
def inicio (request):
    return render(request,'paginas/inicio.html')
def nosotros (request):
    return render(request,'paginas/nosotros.html')
#FIN PAGINAS DEL SITIO------------------------------------------------------------

#TABLA 9 -------------------------------------------------------------------------
def Tabla9 (request):
    Tabla9 = tabla9.objects.all()
    return render(request,'tabla9/index9.html', {'tabla9': Tabla9 })
def crear9 (request):
    formulario = tabla9Form(request.POST or None, request.FILES or None)
    #Con request.Files recepcionamos yluego hacemos el if para guardar y redireccionar a la Tabla9
    if formulario.is_valid():
        formulario.save()
        return redirect(Tabla9)
    return render(request,'tabla9/crear9.html', {'formulario': formulario})
def editar9 (request, id):
    item = tabla9.objects.get(id=id)
    formulario = tabla9Form(request.POST or None, request.FILES or None, instance=item)
    return render(request,'tabla9/editar9.html', {'formulario': formulario})
def eliminar9(request ,id):
    item = tabla9.objects.get(id=id)
    item.delete()
    return redirect(Tabla9)
#FIN TABLA 9 ----------------------------------------------------------------------
def Tabla10 (request):
    Tabla10 = tabla10.objects.all()
    return render(request,'tabla9/index9.html', {'tabla10': Tabla10 })

def crear10 (request):
    formulario = tabla10Form(request.POST or None, request.FILES or None)
    #Con request.Files recepcionamos yluego hacemos el if para guardar y redireccionar a la Tabla10
    if formulario.is_valid():
        formulario.save()
        return redirect(Tabla10)
    return render(request,'tabla10/crear10.html', {'formulario': formulario})

def editar10 (request, id):
    item = tabla10.objects.get(id=id)
    formulario = tabla9Form(request.POST or None, request.FILES or None, instance=item)
    return render(request,'tabla10/editar10.html', {'formulario': formulario})

def eliminar10(request ,id):
    item = tabla10.objects.get(id=id)
    item.delete()
    return redirect(Tabla10)