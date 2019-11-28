from django.db import models

# Create your models here.

class Aeropuerto(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    siglas = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre

class Vuelo(models.Model):
    aeropuerto_salida = models.ForeignKey(Aeropuerto, on_delete=models.CASCADE,related_name="salida")
    fecha_salida = models.DateField("Fecha salida")
    aeropuerto_llegada = models.ForeignKey(Aeropuerto, on_delete=models.CASCADE,related_name="llegada")
    codigo_vuelo = models.CharField(max_length=100, unique=False)

    def __str__(self):
        return self.codigo_vuelo

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField("Fecha nacimiento")

    def __str__(self):
        return  self.nombre

class Reserva(models.Model):
    vuelo = models.ForeignKey('Vuelo', on_delete=models.CASCADE)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    fecha_reserva = models.DateField("Fecha reserva")
    precio = models.DecimalField(decimal_places=2,max_digits=10)

    def __str__(self):
        return str(self.precio)