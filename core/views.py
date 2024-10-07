from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Cerveza


def login(request):
    return render(request, 'home.html', {})

def logout(request):
    logout(request)
    return redirect('login')

@login_required
def who(request):
    return render(request, 'who.html',{})

@login_required
def home(request):
    return render(request, 'home.html', {})

@login_required
def reports(request):
    return render(request, 'reports.html', {})

@login_required
def panel(request):
    return render(request, 'panel.html', {})

@login_required
def about(request):
    return render(request, 'about.html', {})

@login_required
def lista_cervezas(request):
    cervezas = Cerveza.objects.all()
    return render(request, 'cervezas.html', {'cervezas': cervezas})
