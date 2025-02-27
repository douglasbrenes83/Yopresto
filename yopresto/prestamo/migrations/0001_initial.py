# Generated by Django 5.1.3 on 2024-11-27 17:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tasa_interes', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fecha_inicio', models.DateField()),
                ('fecha_vencimiento', models.DateField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prestamos', to='clientes.cliente')),
            ],
        ),
    ]
