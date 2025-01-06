# Register your models here.
from django.contrib import admin
from .models import Prestamo

@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'monto', 'fecha_inicio', 'fecha_vencimiento')
