# Generated by Django 2.2.7 on 2019-11-28 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aeropuerto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=100)),
                ('siglas', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha nacimiento')),
            ],
        ),
        migrations.CreateModel(
            name='Vuelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_salida', models.DateField(verbose_name='Fecha salida')),
                ('codigo_vuelo', models.CharField(max_length=100)),
                ('aeropuerto_llegada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='llegada', to='vuelos.Aeropuerto')),
                ('aeropuerto_salida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salida', to='vuelos.Aeropuerto')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_reserva', models.DateField(verbose_name='Fecha reserva')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vuelos.Cliente')),
                ('vuelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vuelos.Vuelo')),
            ],
        ),
    ]
