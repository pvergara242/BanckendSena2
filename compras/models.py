from django.db import models

# Create your models here.
class Compra(models.Model):
    codigo_comprobante= models.IntegerField(max_length=200)
    numero_factura= models.IntegerField(max_length=200)
    detalle_general= models.CharField(max_length=200)
    fecha_compra= models.DateField(max_length=200)
    codigo_tercero= models.CharField(max_length=200)
    nombre_tercero= models.CharField(max_length=200)
    codigo_producto= models.CharField(max_length=200)
    nombre_productol= models.CharField(max_length=200)
    cantidades= models.IntegerField(max_length=200)
    unidadedisponible= models.CharField(max_length=200)
    coatounitariocompra= models.CharField(max_length=200)
    costototalcompras = models.CharField(max_length=200)
    impuestos = models.CharField(max_length=200)
    totalimpuesto= models.CharField(max_length=200)
    retencionfuente = models.CharField(max_length=200)
    porcentajereflete= models.CharField(max_length=200)
    totalretenciondelafuente = models.CharField(max_length=200)
