from django import forms
from .models import Prestamo,Pago
from clientes.models import Cliente

class PrestamoForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(
        queryset=Cliente.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Cliente"
    )
    
    saldo_actual = forms.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        widget=forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        label="Saldo Actual", 
        required=False
    )

    estado = forms.ChoiceField(
        choices=Prestamo._meta.get_field('estado').choices,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Estado"
    )

    class Meta:
        model = Prestamo
        fields = ['monto', 'tasa_interes', 'fecha_inicio', 'fecha_vencimiento', 'cliente', 'descripcion', 'saldo_actual', 'estado']
        widgets = {
            'monto': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'tasa_interes': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_vencimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        # Asignar el monto al saldo_actual al crear el préstamo
        if not instance.pk:  # Si es un nuevo préstamo
            instance.saldo_actual = instance.monto
        if commit:
            instance.save()
        return instance


class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = ['fecha_pago', 'monto_pagado', 'metodo_pago']
        widgets = {
            'fecha_pago': forms.DateInput(attrs={'type': 'date'}),  # Selector de fecha
        }

    def __init__(self, *args, **kwargs):
        self.prestamo = kwargs.pop('prestamo', None)  # Pasar el préstamo desde la vista
        super().__init__(*args, **kwargs)
        self.fields['metodo_pago'].label = "Método de Pago"

    def clean_monto_pagado(self):
        monto_pagado = self.cleaned_data['monto_pagado']
        if self.prestamo and monto_pagado > self.prestamo.saldo_actual:
            raise forms.ValidationError(
                f"El monto del pago ({monto_pagado}) no puede ser mayor al saldo actual del préstamo ({self.prestamo.saldo_actual})."
            )
        return monto_pagado