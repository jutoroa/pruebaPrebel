from django.db import models

# Create your models here.
class Producto(models.Model):
    codigo_producto = models.CharField(max_length=10)
    nombre_producto = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    fecha_compra = models.DateField()
    numero_factura = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre_producto