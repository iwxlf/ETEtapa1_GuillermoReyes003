from django.shortcuts import redirect, render
from .models import Contacto
from .forms import ContactoForm

# Create your views here.

def home(request):
    return render(request,'home.html',)


def form_crearproveedor(request):
    proveedores = Contacto.objects.all()
    if request.method=='POST': 
        contacto_form = ContactoForm(request.POST)
        if contacto_form.is_valid():
            contacto_form.save()
            return redirect('home')
    else:
        contacto_form= ContactoForm()
    return render(request, 'groundzero/form_crearproveedor.html', {'contacto_form': contacto_form, 'datos':proveedores})

def ver(request):
    proveedores = Contacto.objects.all()
    if request.method=='POST': 
        contacto_form = ContactoForm(request.POST)
        if contacto_form.is_valid():
            contacto_form.save()
            return redirect('home')
    else:
        contacto_form= ContactoForm()
    return render(request, 'groundzero/ver.html', {'contacto_form': contacto_form, 'datos':proveedores})

def modificar_proveedor(request,id):
    contactos = Contacto.objects.get(numero_identificaion=id)

    datos={
        'form':ContactoForm(instance=contactos)
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST, instance = contactos)
        if formulario.is_valid:
            formulario.save()
            return redirect('home')
    return render(request, 'groundzero/modificar_proveedor.html',datos)

def eliminar_proveedor(request,id):
    contactos = Contacto.objects.get(numero_identificaion=id)
    contactos.delete()
    return redirect('home')