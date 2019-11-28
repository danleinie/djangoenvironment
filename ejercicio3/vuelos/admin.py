from django.contrib import admin

# Register your models here.
from vuelos.models import Aeropuerto, Vuelo, Cliente, Reserva


@admin.register(Aeropuerto)
class AeropuertoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ciudad', 'siglas')

@admin.register(Vuelo)
class VueloAdmin(admin.ModelAdmin):
    list_display = ('aeropuerto_salida', 'fecha_salida', 'aeropuerto_llegada', 'codigo_vuelo')
    list_filter = ['fecha_salida']

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'email', 'fecha_nacimiento')

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('vuelo', 'cliente', 'fecha_reserva', 'precio')
