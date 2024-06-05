from django.db import models

# Create your models here.
#tabla 9: Código de la cuenta contable
class tabla9(models.Model):
    id = models.AutoField(primary_key=True)
    N9 = models.IntegerField( verbose_name='N°', default="")  # Add default value here
    Descripcion9 = models.TextField(null=True, verbose_name='Descripción')

def __str__(self):
    fila =  "Descripción " + self.Descripcion
    return fila

#Tabla 10: Tipo de comprobante de pago o documento
class tabla10(models.Model):
    id = models.AutoField(primary_key=True)
    num = models.IntegerField(verbose_name='N°', default="")
    Desc = models.TextField(null=True, verbose_name='Descripción')
