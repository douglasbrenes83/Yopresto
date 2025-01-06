from django.db import models

# Create your models here.
from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=50, unique=True)
    direccion = models.TextField()
    edad = models.PositiveIntegerField()
    sexo = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Femenino')])
    telefono = models.CharField(max_length=15)
    foto = models.ImageField(upload_to='clientes/fotos/', blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre
    
    
