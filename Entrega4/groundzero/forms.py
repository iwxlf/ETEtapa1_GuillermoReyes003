from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import TipoMoneda, Contacto


class ContactoForm(forms.ModelForm):

    class Meta: 
        model= Contacto
        fields = ['numero_identificaion', 'nombre_completo', 'telefono', 'direccion', 'email' , 'pais','contraseña','moneda']
        labels ={
            'numero_identificaion': ' Ingrese su Numero de Identificacion:', 
            'nombre_completo': 'Ingrese su Nombre completo:', 
            'telefono': 'Ingrese su Telefono:', 
            'direccion': 'Ingrese su Direccion:',
            'email': 'Ingrese su Email:',
            'pais': 'Ingrese su Pais:',
            'contraseña': 'Ingrese su Contraseña',
            'moneda': 'Ingrese su Moneda',
        }
        widgets={
            'numero_identificaion': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Numero de Identificacion', 
                    'id': 'numero_identificaion',
                    'name': 'numero_identificaion',
                    
                    
                }
            ), 
            'nombre_completo': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Nombre Completo', 
                    'id': 'nombre_completo',
                    'name': 'nombre_completo',
                }
            ), 
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Telefono', 
                    'id': 'telefono',
                    'name': 'telefono',
                }
            ), 
            
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Direccion', 
                    'id': 'direccion',
                    'name': 'direccion',
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Email', 
                    'id': 'email',
                    'name': 'email',
                    'type': 'email',
                }
            ), 
            'pais': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Pais', 
                    'id': 'pais',
                    'name': 'pais',
                }
            ), 
            'contraseña': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Contraseña', 
                    'id': 'pais',
                    'name': 'contraseña',
                    'type': 'password'
                }
            ), 
            'moneda': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'moneda',
                    'name': 'moneda'
                }
            ),

        }