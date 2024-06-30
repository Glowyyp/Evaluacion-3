from django.shortcuts import render
from .models import Nav, Servicio, Quienesomo

# Create your views here.

def home(request):
    navbar = Nav.objects.all()
    context = {'navbar':navbar}
    return render(request, 'pages/index.html', context)


def QuieneSomos(request):
    navbar = Nav.objects.all()
    nosotros = Quienesomo.objects.all()
    context = {'navbar':navbar, 'nosotros':nosotros}
    return render(request, 'pages/QuienesSomos.html', context)


def servicios(request):
    navbar = Nav.objects.all()
    servicios = Servicio.objects.all()
    context = {'navbar':navbar, 'servicios':servicios}
    return render(request, 'pages/Servicios.html', context)