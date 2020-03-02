from django.http import HttpResponse
from django.shortcuts import render
from .models import Dato 
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/accounts/login/")
def lista_datos(request):
    datos = Dato.objects.all().order_by('date')
    return render(request, 'datos/lista_datos.html', {'datos': datos })

@login_required(login_url="/accounts/login/")
def detalle_datos(request, slug):
    dato = Dato.objects.get(slug=slug)
    return render(request, 'datos/detalle_datos.html', {'dato': dato })