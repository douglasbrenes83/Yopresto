# Generated by Django 5.1.3 on 2024-11-27 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('cedula', models.CharField(max_length=50, unique=True)),
                ('direccion', models.TextField()),
                ('edad', models.PositiveIntegerField()),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=10)),
                ('telefono', models.CharField(max_length=15)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='clientes/fotos/')),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
