from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio , name='inicio'),
    path('diario', views.diario , name='diario'),
    path('ventas', views.ventas , name='ventas'),
    path('compras', views.compras , name='compras'),
    path('nosotros', views.nosotros, name='nosotros'),

    path('libros', views.libros, name='libros'),
    path('libros/crear', views.crear_codigo, name='crear'),
    path('libros/editar', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('libros/editar/<int:id>', views.editar, name='editar'),

    path('libro9', views.libro9, name='libro9'),
    path('libro9/crear', views.crear9, name='crear9'),
    path('libro9/editar', views.editar9, name='editar9'),
    path('eliminar9/<int:id>', views.eliminar9, name='eliminar9'),
    path('libro9/editar/<int:id>', views.editar9, name='editar9'),
]