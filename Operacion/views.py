from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductoForm, VentaForm, ClienteForm, AsesorForm, LoginForm
from django.contrib.auth import authenticate, login #PasswordResetView
from .models import Producto, Venta
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

#from django.contrib.auth import PasswordResetView


# para volver a la pagina de inicio.
def index_view(request):
    return render(request, 'inicio.html')
  
# Para ingresar a la pagina de inicio
@login_required
def inicio_view(request):
  return render(request, 'inicio.html')

# Para el inicio de sesión del usuario - pide contraseña y código del asesor

def login_view(request):
  if request.method == 'POST':
      form = LoginForm(request.POST)
      if form.is_valid():
          username = form.cleaned_data['codigo']
          password = form.cleaned_data['contrasena']
          user = authenticate(request, username=username, password=password)
          print(user)
          if user is not None:
                login(request, user)
                # Redireccionar a la página de inicio después del inicio de sesión
                return HttpResponse("Inicio de sesión exitoso. Redirigiendo a la página principal...")
  
  else:
        form = LoginForm()
  return render(request, 'inicio.html', {'form': form})
  
# Para registrar nuevos productos
@login_required
def registrar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')  # Redirige a la lista de productos después de registrar uno nuevo
    else:
        form = ProductoForm()
    return render(request, 'registrar_producto.html', {'form': form})
  
# Para ver listado de productos y que permita eliminar
@login_required
def lista_productos(request):
    productos = Producto.objects.all()
    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')  # Obtener el ID del producto a eliminar del formulario
        producto = Producto.objects.get(pk=producto_id)  # Obtener el producto por su ID
        producto.delete()  # Eliminar el producto
        return redirect('lista_productos')  # Redirigir a la lista de productos después de eliminar el producto
    return render(request, 'lista_productos.html', {'productos': productos})
  

# Para editar las ventas
@login_required
def registrar_venta(request):
  if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_ventas')  # Redirige a la página de lista de ventas
  else:
        form = VentaForm()
  return render(request, 'registrar_venta.html', {'form': form})

# Para registrar un cliente en el sistema.
@login_required
def registrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registrar_venta')  # Redirige a la página de inicio después de registrar el cliente
    else:
        form = ClienteForm()
    return render(request, 'registrar_cliente.html', {'form': form})
  
# Para registrar asesor en el sistema.
@login_required
def registrar_asesor(request):
    if request.method == 'POST':
        form = AsesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')  # Redirige a la página de inicio después de registrar el asesor
    else:
        form = AsesorForm()
    return render(request, 'registrar_asesor.html', {'form': form})
  
  
  # Para generar reporte de ventas y que permita eliminar la venta si se requiere.
@login_required
def lista_ventas(request):
    ventas = Venta.objects.all()
    if request.method == 'POST':
        venta_id = request.POST.get('venta_id')  # Obtener el ID de la venta a eliminar del formulario
        venta = Venta.objects.get(pk=venta_id)  # Obtener la venta por su ID
        venta.delete()  # Eliminar la venta
        return redirect('lista_ventas')  # Redirigir a la lista de ventas después de eliminar la venta
    return render(request, 'lista_ventas.html', {'ventas': ventas})
  
def eliminar_venta(request, venta_id):
  venta = get_object_or_404(Venta, id=venta_id)
  venta.delete()
    # Redireccionar a alguna página después de eliminar la venta
  return redirect('lista_ventas')


# Eliminar el producto
@login_required
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'editar_producto.html', {'form': form})
