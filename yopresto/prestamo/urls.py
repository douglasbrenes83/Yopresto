from django.urls import path
from .views import (PrestamoListView, PrestamoCreateView,PrestamoUpdateView,PrestamoDeleteView,PagoCreateView,PrestamoPagosDetailView,PrestamoActivoListView,pagos_por_rango,)
from .viewsaldo import DetallePrestamoView

urlpatterns = [
    path('', PrestamoListView.as_view(), name='prestamo_list'),
    path('nuevo/', PrestamoCreateView.as_view(), name='prestamo_create'),
    path('<int:pk>/editar/', PrestamoUpdateView.as_view(), name='editar_prestamo'),
    path('<int:pk>/eliminar/',PrestamoDeleteView.as_view(), name='prestamo_delete'),
    path('<int:prestamo_id>/pagos/nuevo/', PagoCreateView.as_view(), name='pago_create'),
    path('<int:pk>/detalle/', PrestamoPagosDetailView.as_view(), name='prestamo_pagos'),
    path('<int:pk>/saldo/', DetallePrestamoView.as_view(), name='detalle_prestamo'),
    path('activos/', PrestamoActivoListView.as_view(), name='prestamo_activos'),
    path('pagos_por_rango/', pagos_por_rango, name='pagos_por_rango'), 

]
