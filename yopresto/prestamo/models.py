from django.db import models
from clientes.models import Cliente

# Variable global para contar las actualizaciones
contador_actualizaciones = 0

class Prestamo(models.Model):
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    tasa_interes = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_inicio = models.DateField()
    fecha_vencimiento = models.DateField()
    saldo_actual = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(
        max_length=10,
        choices=[
            ('activo', 'Activo'),
            ('cancelado', 'Cancelado'),
            ('atrasado', 'Atrasado')
        ],
        default='activo'
    )
    descripcion = models.TextField(null=True, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"Préstamo {self.id} - {self.cliente.nombre}"

    def actualizar_saldo(self, monto_pagado):
        """Actualiza el saldo del préstamo y cambia su estado."""
        global contador_actualizaciones
        contador_actualizaciones += 1  # Incrementa el contador

        # Log para depuración
        print(f"Actualizando saldo del préstamo {self.id}: "
              f"monto pagado = {monto_pagado}, "
              f"llamadas hasta ahora = {contador_actualizaciones}")

        self.saldo_actual -= monto_pagado
        if self.saldo_actual <= 0:
            self.saldo_actual = 0
            self.estado = 'Cancelado'
        else:
            self.estado = 'Activo'
        self.save()

class Pago(models.Model):
    METODOS_PAGO = [
        ('Efectivo', 'Efectivo'),
        ('Tarjeta de Crédito', 'Tarjeta de Crédito'),
        ('Tarjeta de Débito', 'Tarjeta de Débito'),
        ('Transferencia Bancaria', 'Transferencia Bancaria'),
        ('Otro', 'Otro'),
    ]

    prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE, related_name='pagos')
    fecha_pago = models.DateField()
    monto_pagado = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=50, choices=METODOS_PAGO)

    def __str__(self):
        return f"Pago {self.pk} - Préstamo {self.prestamo.id}"

    def save(self, *args, **kwargs):
        # Log para depuración
        print(f"Guardando pago {self.pk} para préstamo {self.prestamo.id}: monto pagado = {self.monto_pagado}")
        
        # Llama al método save del modelo
        super().save(*args, **kwargs)
        
        # Actualiza el saldo del préstamo
        self.prestamo.actualizar_saldo(self.monto_pagado)



