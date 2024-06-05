from django.db import models

# Create your models here.

class tabla9(models.Model):
    id = models.AutoField(primary_key=True)
    N9 = models.CharField(max_length=100, verbose_name="N°",default="")
    Descripcion9 = models.TextField(null=True, verbose_name="Descripción")

def __str__(self):
    fila = "N: " + self.N9 + " - Descripcion: " + self.Descripcion9
    return fila

class tabla10(models.Model):
    id = models.AutoField(primary_key=True)
    N10 = models.CharField(max_length=100, verbose_name="N°",default="")
    Descripcion10 = models.TextField(null=True, verbose_name="Descripción")
