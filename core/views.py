from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from .models import Cerveza

def who(request):
    return render(request, 'who.html',{})

def login(request):
    return render(request, 'login.html', {})

def home(request):
    return render(request, 'home.html', {})

def reports(request):
    return render(request, 'reports.html', {})

def panel(request):
    return render(request, 'panel.html', {})

def about(request):
    return render(request, 'about.html', {})

def lista_cervezas(request):
    cervezas = Cerveza.objects.all()
    return render(request, 'cervezas.html', {'cervezas': cervezas})
