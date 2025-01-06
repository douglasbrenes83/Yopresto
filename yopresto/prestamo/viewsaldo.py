from django.shortcuts import render
from django.views.generic import DetailView
from .models import Prestamo, Pago

class DetallePrestamoView(DetailView):
    model = Prestamo
    template_name = 'saldo_pendiente.html'
    context_object_name = 'prestamo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pagos = Pago.objects.filter(prestamo=self.object)
        total_pagado = sum(pago.monto_pagado for pago in pagos)
        saldo_pendiente = self.object.monto - total_pagado
        context['pagos'] = pagos
        context['total_pagado'] = total_pagado
        context['saldo_pendiente'] = saldo_pendiente
        return context