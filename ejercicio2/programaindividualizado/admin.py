from django.contrib import admin

# Register your models here.
from programaindividualizado.models import Residente, Familiar, Informe, ParteInforme


@admin.register(Residente)
class ResidenteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'fecha_nacimiento')
    list_filter = ['fecha_nacimiento']

@admin.register(Familiar)
class FamiliarAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'fecha_nacimiento', 'parentesto')
    list_filter = ['fecha_nacimiento']

@admin.register(Informe)
class InformeAdmin(admin.ModelAdmin):
    list_display = ['fecha_uniforme']
    list_filter = ['fecha_uniforme']

@admin.register(ParteInforme)
class ParteInformeAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'valoracion_inicial', 'objetivos')
    list_filter = ['valoracion_inicial']