from django.db import models

# Create your models here.

class Inventario(models.Model):
    cod_producto=models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    cantidad_disponible = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class Vendedor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
class Venta(models.Model):
    producto = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    cantidad_vendida = models.IntegerField()
    fecha_venta = models.DateTimeField(auto_now_add=True)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    

    def __str__(self):
        return f'{self.cantidad_vendida} x {self.producto.nombre} ({self.fecha_venta}) por {self.vendedor.nombre} {self.vendedor.apellido}'