from django.contrib import admin
from .models import Producto, Categoria;

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio_unidad', 'categoria')


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria_padre')


admin.site.register(Producto,ProductoAdmin);
admin.site.register(Categoria,CategoriaAdmin);
