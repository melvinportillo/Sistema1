# Generated by Django 3.2.6 on 2021-10-13 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Balance_General',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cuenta', models.CharField(max_length=50)),
                ('Saldo', models.FloatField()),
                ('Activo', models.FloatField()),
                ('Pasivo', models.FloatField()),
                ('Total', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Estado_Resultado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cuenta', models.CharField(max_length=50)),
                ('Fecha_1', models.FloatField()),
                ('Fecha_2', models.FloatField()),
                ('Saldo', models.FloatField()),
                ('Rojo', models.FloatField()),
                ('Amarillo', models.FloatField()),
                ('Verde', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Libro_Diario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Usuario', models.CharField(max_length=20)),
                ('Fecha', models.DateField()),
                ('Descripcion', models.CharField(max_length=100)),
                ('Debe', models.CharField(max_length=150)),
                ('Haber', models.CharField(max_length=150)),
                ('Cuadre', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Libro_Mayor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cuenta', models.CharField(max_length=50)),
                ('Debe', models.FloatField()),
                ('Haber', models.FloatField()),
                ('Fecha', models.DateField()),
                ('Cuadre', models.FloatField()),
                ('Descripcion', models.CharField(max_length=100)),
            ],
        ),
    ]
