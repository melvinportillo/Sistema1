# Generated by Django 3.2.6 on 2021-10-13 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acciones_Prestamos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_prestamo', models.IntegerField()),
                ('num_cuota', models.IntegerField()),
                ('Fecha_Pago', models.DateField()),
                ('Num_recibo', models.IntegerField()),
                ('Monto', models.FloatField()),
                ('Capital', models.FloatField()),
                ('Descuento', models.FloatField()),
                ('Intereses', models.FloatField()),
                ('Pago', models.FloatField()),
                ('Saldo', models.FloatField()),
                ('Saldo_mora', models.FloatField()),
                ('Intereses_moratorios', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Datos_prestamos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_cliente', models.CharField(max_length=15)),
                ('id_prestamo', models.IntegerField()),
                ('nombre_cliente', models.CharField(max_length=50)),
                ('miembro', models.CharField(max_length=1)),
                ('fecha_otorgado', models.DateField()),
                ('fecha_vencimiento', models.DateField()),
                ('plazo_meses', models.IntegerField()),
                ('taza_mensual', models.FloatField()),
                ('Periodo_Gracia', models.IntegerField()),
                ('Taza_Descuento', models.FloatField()),
                ('Monto', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Temp_Acciones_Prestamos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Usuario', models.CharField(max_length=15)),
                ('num_cuota', models.IntegerField()),
                ('fecha_cuota', models.DateField()),
                ('capital', models.FloatField()),
                ('Descuento', models.FloatField()),
                ('Intereses', models.FloatField()),
                ('total_cuota', models.FloatField()),
                ('saldo', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Temp_Datos_prestamos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Usuario', models.CharField(max_length=15)),
                ('id_persona', models.CharField(max_length=15)),
                ('nombre_cliente', models.CharField(max_length=50)),
                ('miembro', models.CharField(max_length=1)),
                ('fecha_otorgado', models.DateField()),
                ('plazo_meses', models.IntegerField()),
                ('taza_mensual', models.FloatField()),
                ('Intereses', models.FloatField()),
                ('Periodo_Gracia', models.IntegerField()),
                ('Taza_Descuento', models.FloatField()),
                ('Monto', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Variables_Generales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variable', models.CharField(max_length=50)),
                ('valor', models.CharField(max_length=50)),
            ],
        ),
    ]
