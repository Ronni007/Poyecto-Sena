from django.urls import path,include
from . import views
from .views import login_view, inicio_view,index_view, eliminar_venta, editar_producto


urlpatterns = [
    path('', index_view, name='index'),
    path('login/', login_view, name='login_view'),
    path('inicio/', inicio_view, name='inicio'),
    path('registrar_producto/', views.registrar_producto, name='registrar_producto'),
    path('lista_productos/', views.lista_productos, name='lista_productos'),
    path('registrar_venta/', views.registrar_venta, name='registrar_venta'),
    path('registrar_cliente/', views.registrar_cliente, name='registrar_cliente'),
    path('registrar_asesor/', views.registrar_asesor, name='registrar_asesor'),
    path('lista_ventas/', views.lista_ventas, name='lista_ventas'),
    path('accounts/', include ('django.contrib.auth.urls')),
    path('eliminar-venta/<int:venta_id>/', eliminar_venta, name='eliminar_venta'),
    path('editar-producto/<int:producto_id>/', editar_producto, name='editar_producto'),

    ]