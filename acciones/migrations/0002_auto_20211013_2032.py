# Generated by Django 3.2.6 on 2021-10-13 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acciones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temp_acciones_accionista',
            name='Usuario',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='temp_datos_accionista',
            name='Usuario',
            field=models.CharField(max_length=50),
        ),
    ]