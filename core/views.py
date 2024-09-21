from django.shortcuts import render
from .models import Cerveza

def login(request):
    return render(request, 'login.html', {})

def lista_cervezas(request):
    cervezas = Cerveza.objects.all()
    return render(request, 'cervezas.html', {'cervezas': cervezas})
    

