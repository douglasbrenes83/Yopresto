from django.urls import path
from .views import ClienteListView, ClienteCreateView,ClienteDeleteView,ClienteUpdateView

urlpatterns = [
   
    path('', ClienteListView.as_view(), name='cliente_list'),
    path('nuevo/', ClienteCreateView.as_view(), name='cliente_create'),
    path('cliente/<int:pk>/editar/', ClienteUpdateView.as_view(), name='editar_cliente'),
    path('cliente/<int:pk>/eliminar/', ClienteDeleteView.as_view(), name='eliminar_cliente'),

]
