from django.db import models

# Create your models here.

7
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    url_imagen = models.CharField(max_length=1000)
    precio_unidad = models.DecimalField(max_digits=6,decimal_places=2)
    categoria = models.ForeignKey('Categoria',on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre





class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    categoria_padre = models.ForeignKey('Categoria', on_delete=models.CASCADE, blank=True,null=True)

    def __str__(self):
        return self.nombre