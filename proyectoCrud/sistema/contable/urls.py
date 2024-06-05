from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),

    #ENLACES TABLA 9------------------------------------------------------------------
    path('tabla9', views.Tabla9, name='tabla9'),
    path('tabla9/crear9', views.crear9, name='crear9'),
    path('tabla9/editar9', views.editar9, name='editar9'),
    path('eliminar9/<int:id>', views.eliminar9, name='eliminar9'),
    path('tabla9/editar9/<int:id>', views.editar9, name='editar9'),
    #FIN ENLACES TABLA 9--------------------------------------------------------------
    #ENLACES TABLA 10------------------------------------------------------------------
    path('tabla10', views.Tabla10, name='tabla10'),
    path('tabla10/crear10', views.crear10, name='crear10'),
    path('tabla10/editar', views.editar10, name='editar10'),
    path('eliminar10/<int:id>', views.eliminar10, name='eliminar10'),
    path('tabla10/editar10/<int:id>', views.editar10, name='editar10'),
]