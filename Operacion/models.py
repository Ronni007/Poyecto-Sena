from django.db import models


# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=0)
    descripcion = models.TextField()
    

    def __str__(self):
        return self.nombre

class Asesor(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    correo = models.EmailField()
    contrasena = models.CharField(max_length=15)
    tasa_comision = models.DecimalField(max_digits=5, decimal_places=2)

    #Calcular comision total del asesor multiplicando la tasa con el valor del producto.

    def __str__(self):
        return self.codigo

class Cliente(models.Model):
    nit = models.CharField(max_length=15, primary_key=True)
    nombre = models.CharField(max_length=60)
    contador = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Venta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    asesor = models.ForeignKey(Asesor, on_delete=models.CASCADE)
    fecha = models.DateField()
    nit_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    contador = models.CharField(max_length=20)
    

    def __str__(self):
        return f"Venta de {self.producto.nombre} a {self.cliente.nombre} por {self.asesor.codigo}"