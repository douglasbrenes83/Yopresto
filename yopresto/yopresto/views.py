from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views import View
from prestamo.models import Prestamo
from datetime import date


class ResLogin(View):
    def get(self, request):
        return render(request, 'index/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirige a la página de inicio o dashboard
        else:
            return render(request, 'index/login.html', {'error_message': 'Credenciales inválidas'})
class LogoutView(View):
    def get(self, request, *args, **kwargs):
        # Cierra la sesión del usuario actual
        logout(request)
        # Agrega un mensaje de éxito
        messages.success(request, "Has cerrado sesión exitosamente.")
        # Redirige a la página de login
        return redirect('ResLogin')  # Cambia 'index' por el nombre correcto de tu vista de login
    
class DashboardView(LoginRequiredMixin,View):
    login_url = 'index' 
    def get(self, request):
        # Obtener la fecha de hoy
        fecha_hoy = date.today()

        # Filtrar los préstamos vencidos hoy
        prestamos_vencidos_hoy = Prestamo.objects.filter(fecha_vencimiento=fecha_hoy)

        # Contar el número de préstamos vencidos hoy
        cantidad_prestamos_vencidos = prestamos_vencidos_hoy.count()

        # Pasar los datos al contexto
        context = {
            'cantidad_prestamos_vencidos': cantidad_prestamos_vencidos,
            'prestamos_vencidos_hoy': prestamos_vencidos_hoy  # Agregamos la lista de préstamos vencidos
        }

        # Renderizar la plantilla con el contexto
        
        return render(request, 'Dashboard/dashboard.html', context)


