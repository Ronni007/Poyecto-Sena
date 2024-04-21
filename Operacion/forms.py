from django import forms
from .models import Producto, Asesor, Cliente, Venta
from datetime import date



class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'valor', 'descripcion']
        

class AsesorForm(forms.ModelForm):
    class Meta:
      model = Asesor
      fields = ['codigo', 'correo' , 'tasa_comision', 'contrasena']
      
class ClienteForm(forms.ModelForm):
  class Meta:
    model = Cliente
    fields = ['nit', 'nombre', 'contador']
    
class VentaForm(forms.ModelForm):
  fecha = forms.DateField(
        widget=forms.DateInput(attrs={'value': date.today().strftime('%Y-%m-%d')}),
        label='Fecha de venta')
  class Meta:
    model = Venta
    fields = ['producto', 'asesor','nit_cliente','contador','fecha']
    

class LoginForm(forms.Form):
    codigo = forms.CharField(label='Código de usuario', max_length=100)
    contrasena = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    

class editarProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'valor', 'descripcion']