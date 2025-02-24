from django.urls import path
from .views import (PrestamoListView, PrestamoCreateView,PrestamoUpdateView,PrestamoDeleteView,PagoCreateView,PrestamoPagosDetailView,PrestamoActivoListView,exportar_prestamos_vencidos,prestamos_vencidos,descargar_reporte_excel,reporte_prestamos,pagos_por_rango,nuevo_prestamo)
from .viewsaldo import DetallePrestamoView

urlpatterns = [
    path('', PrestamoListView.as_view(), name='prestamo_list'),
    path('nuevo/', PrestamoCreateView.as_view(), name='prestamo_create'),
    path('nuevo_prestamo/<int:cliente_id>/', nuevo_prestamo, name='nuevo_prestamo'),
    path('<int:pk>/editar/', PrestamoUpdateView.as_view(), name='editar_prestamo'),
    path('<int:pk>/eliminar/',PrestamoDeleteView.as_view(), name='prestamo_delete'),
    path('<int:prestamo_id>/pagos/nuevo/', PagoCreateView.as_view(), name='pago_create'),
    path('<int:pk>/detalle/', PrestamoPagosDetailView.as_view(), name='prestamo_pagos'),
    path('<int:pk>/saldo/', DetallePrestamoView.as_view(), name='detalle_prestamo'),
    path('activos/', PrestamoActivoListView.as_view(), name='prestamo_activos'),
    path('pagos_por_rango/', pagos_por_rango, name='pagos_por_rango'), 
    path('reporte-prestamos/', reporte_prestamos, name='reporte_prestamos'),
    path('descargar-reporte-excel/', descargar_reporte_excel, name='descargar_reporte_excel'),
    path('prestamos_vencidos/', prestamos_vencidos, name='prestamos_vencidos'),
    path('exportar_prestamos_vencidos/', exportar_prestamos_vencidos, name='exportar_prestamos_vencidos'),


]
