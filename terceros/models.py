from django.db import models

# Create your models here.
class Tercero(models.Model):
    documento= models.IntegerField(max_length=200)
    primer_nombre= models.CharField(max_length=200)
    segundo_nombre= models.CharField(max_length=200)
    primer_apellido = models.CharField(max_length=200)
    segundo_apellido= models.CharField(max_length=200)
    tipo_usuario = models.CharField(max_length=200)
    razon_social = models.CharField(max_length=200)
    codigo_pais= models.CharField(max_length=200)
    codig_departamento = models.CharField(max_length=200)
    codigo_mucipio= models.CharField(max_length=200)
    direccion= models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    correo_electronico = models.EmailField(max_length=200)
