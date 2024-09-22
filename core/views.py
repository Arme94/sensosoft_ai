from django.shortcuts import render
from .models import Cerveza

def login(request):
    return render(request, 'login.html', {})

def home(request):
    return render(request, 'home.html', {})

def users(request):
    return render(request, 'users.html', {})

def reports(request):
    return render(request, 'reports.html', {})

def panel(request):
    return render(request, 'panel.html', {})

def about(request):
    return render(request, 'about.html', {})

def lista_cervezas(request):
    cervezas = Cerveza.objects.all()
    return render(request, 'cervezas.html', {'cervezas': cervezas})
    


