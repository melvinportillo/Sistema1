# Generated by Django 3.2.6 on 2021-10-13 20:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Codigo', models.CharField(max_length=15)),
                ('Descripcion', models.CharField(max_length=50)),
                ('Fecha_Ingreso', models.DateField(default=datetime.datetime(2021, 10, 13, 20, 24, 1, 836315, tzinfo=utc))),
                ('Valor', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Temp_Inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Usuario', models.CharField(max_length=15)),
                ('Codigo', models.CharField(max_length=15)),
                ('Descripcion', models.CharField(max_length=50)),
                ('Fecha_Ingreso', models.DateField(default=datetime.datetime(2021, 10, 13, 20, 24, 1, 836630, tzinfo=utc))),
                ('Valor', models.FloatField()),
            ],
        ),
    ]
