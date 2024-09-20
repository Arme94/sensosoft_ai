from django.shortcuts import render
from .models import Cerveza

def lista_cervezas(request):
    cervezas = Cerveza.objects.all()
    return render(request, 'core/cervezas.html', {'cervezas': cervezas})

