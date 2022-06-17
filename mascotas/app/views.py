from django.shortcuts import render

from app.models import Contacto
from .forms import ContactoForm

# Create your views here.
def home(request):
    return render(request, 'app/home.html')

def contacto(request):
    data = {
        'form': ContactoForm()
    }
    
    if request.method == 'POST':
        formulario =ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Mensaje enviado"
        else:
            data["form"] = formulario
            
    return render(request, 'app/contacto.html',data)

def comida(request):
    return render(request, 'app/comida.html')

def accesorios(request):
    return render(request, 'app/accesorios.html')

def listar_contactos(request):
    contacto = Contacto.objects.all()
    
    data={
        'contacto': contacto
        
    }
    return render(request, 'app/producto/listar.html',data)