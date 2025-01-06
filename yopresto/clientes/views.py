from django.shortcuts import render,redirect,get_object_or_404
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.views.generic import CreateView, ListView,DeleteView,UpdateView
from django.urls import reverse_lazy
from .models import Cliente
from .forms import ClienteForm

class ClienteListView(LoginRequiredMixin,ListView):
    login_url = 'index' 
    model = Cliente
    template_name = 'clientes/cliente_list.html'
    context_object_name = 'clientes'

class ClienteCreateView(LoginRequiredMixin,CreateView):
    login_url = 'index' 
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/cliente_form.html'
    success_url = reverse_lazy('cliente_list')
    

class ClienteDeleteView(LoginRequiredMixin,DeleteView):
    login_url = 'index' 
    model = Cliente
    template_name = 'clientes/eliminar_cliente.html'
    success_url = reverse_lazy('cliente_list')

class ClienteUpdateView(LoginRequiredMixin,UpdateView):
    login_url = 'index' 
    model = Cliente
    template_name = 'clientes/cliente_form.html'
    fields = ['nombre', 'cedula', 'direccion', 'edad', 'sexo', 'telefono', 'foto', 'descripcion']
    success_url = reverse_lazy('cliente_list')


