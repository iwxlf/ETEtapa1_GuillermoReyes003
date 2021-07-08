from django.urls import path
from .views import home, form_crearproveedor, ver, modificar_proveedor, eliminar_proveedor

urlpatterns=[
    path('home', home, name='home'),
    path('form_crearproveedor', form_crearproveedor, name='form_crearproveedor'),
    path('ver', ver, name= 'ver'),
    path('modificar_proveedor/<id>', modificar_proveedor, name='modificar_proveedor'),
    path('eliminar_proveedor/<id>', eliminar_proveedor, name='eliminar_proveedor'),
]