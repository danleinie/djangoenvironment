from django.db import models

# Create your models here.

class Residente (models.Model):
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=400)
    fecha_nacimiento = models.DateField('date')

    def _str_(self):
        return self.nombre

class Familiar (models.Model):
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=400)
    fecha_nacimiento = models.DateField('date')
    parentesto = models.CharField(max_length=200)

    def _str_(self):
        return self.nombre

class Informe (models.Model):
    fecha_uniforme = models.DateField('date')
    partes_informe = models.ManyToOneRel('ParteInforme',to='ParteInforme',field_name="Partes uniforme")

    def _str_(self):
        return self.fecha_uniforme

class ParteInforme(models.Model):
    TIPOS = (
        ('s', 'SANTIARIA'),
        ('f', 'FUNCIONAL'),
        ('p', 'PSIQUICA'),
        ('so', 'SOCIAL'),
        ('t', 'TERAPIA OCUPACIONAL'),
    )

    tipo = models.CharField(max_length=2, choices=TIPOS, blank=True, default='s', help_text='Tipos')
    valoracion_inicial = models.DecimalField(max_digits=6,decimal_places=2)
    objetivos = models.CharField(max_length=200)


    def _str_(self):
        return self.tipo