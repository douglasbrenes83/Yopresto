from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
# Create your views here.
# prestamos/views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Pago,Prestamo
from .forms import PrestamoForm,PagoForm
from django.utils.dateparse import parse_date
from datetime import datetime
from django.http import JsonResponse
from django.db.models import Sum

class PrestamoListView(LoginRequiredMixin,ListView):
    login_url = 'index' 
    model = Prestamo
    template_name = 'prestamos/prestamo_list.html'
    context_object_name = 'prestamos'

class PrestamoCreateView(LoginRequiredMixin,CreateView):
    login_url = 'index' 
    model = Prestamo
    form_class = PrestamoForm
    template_name = 'prestamos/prestamo_form.html'
    success_url = reverse_lazy('prestamo_list')

class PrestamoUpdateView(LoginRequiredMixin,UpdateView):
    login_url = 'index' 
    model = Prestamo
    form_class = PrestamoForm
    template_name = 'prestamos/editar_prestamo.html'
    success_url = reverse_lazy('prestamo_list')

    def form_valid(self, form):
        monto = form.cleaned_data['monto']
        tasa_interes = form.cleaned_data['tasa_interes']
        # Recalcular saldo_actual
        form.instance.saldo_actual = monto + (monto * tasa_interes / 100)
        return super().form_valid(form)


class PrestamoDeleteView(LoginRequiredMixin,DeleteView):
    login_url = 'index'
    model = Prestamo
    template_name = 'prestamos/prestamo_delete.html'
    success_url = reverse_lazy('prestamo_list')

#pagos

class PrestamoPagosDetailView(LoginRequiredMixin,DetailView):
    login_url = 'index'
    model = Prestamo
    template_name = 'prestamos/detalle_prestamo.html'
    context_object_name = 'prestamo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        prestamo = self.object
        context['pagos'] = prestamo.pagos.all()  # Obtener todos los pagos relacionados con este préstamo
        return context
    
class PagoCreateView(LoginRequiredMixin,CreateView):
    login_url = 'index'
    model = Pago
    form_class = PagoForm
    template_name = 'pagos/pago_create.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        prestamo = get_object_or_404(Prestamo, id=self.kwargs['prestamo_id'])
        kwargs['prestamo'] = prestamo  # Pasar el préstamo al formulario
        return kwargs

    def form_valid(self, form):
        prestamo = get_object_or_404(Prestamo, id=self.kwargs['prestamo_id'])
        form.instance.prestamo = prestamo
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        prestamo = get_object_or_404(Prestamo, id=self.kwargs['prestamo_id'])
        context['prestamo'] = prestamo
        return context

    def get_success_url(self):
        return reverse_lazy('prestamo_pagos', kwargs={'pk': self.object.prestamo.id})

class PrestamoActivoListView(LoginRequiredMixin,ListView):
    login_url = 'index'
    model = Prestamo
    template_name = 'prestamos/prestamo_activos.html'
    context_object_name = 'prestamos'

    def get_queryset(self):
        # Filtra solo los préstamos activos
        return Prestamo.objects.filter(estado="Activo")
    
def pagos_por_rango(request):
    pagos = []
    total_pagado = 0
    fecha_inicio = None
    fecha_fin = None

    if request.method == "GET":
        fecha_inicio = request.GET.get('fecha_inicio')
        fecha_fin = request.GET.get('fecha_fin')

        if fecha_inicio and fecha_fin:
            try:
                # Convertir las fechas de string a objetos de fecha
                fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d').date()
                fecha_fin = datetime.strptime(fecha_fin, '%Y-%m-%d').date()

                # Filtrar pagos dentro del rango
                pagos = Pago.objects.filter(fecha_pago__range=(fecha_inicio, fecha_fin)).select_related('prestamo')

                # Sumar el total de los pagos en ese rango de fechas
                total_pagado = pagos.aggregate(Sum('monto_pagado'))['monto_pagado__sum'] or 0
            except ValueError:
                # Manejar error si las fechas tienen formato incorrecto
                return render(request, 'error.html', {'mensaje': 'Fechas no válidas'})

    # Preparar el contexto para la plantilla
    context = {
        'fecha_inicio': fecha_inicio,
        'fecha_fin': fecha_fin,
        'pagos': pagos,
        'total_pagado': total_pagado,
    }
   
    return render(request, 'prestamos/pagos_rango.html', context)