import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout  # Importa logout con un alias
from django.contrib.auth import logout
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Beer
##from .models import Cerveza

def login(request):
    return render(request, 'login.html', {})  # Asegúrate de usar la plantilla de login

def logout_view(request):
    auth_logout(request)
    return redirect('login')

def login(request):
    return render(request, 'home.html', {})

def logout(request):    
    logout(request)
    storage = messages.get_messages(request)
    storage.used = True  # Marca todos los mensajes como usados
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

def get_sensorial_data(request):
    data = Beer.get_average_sensory_data()
    return JsonResponse(data)

@csrf_exempt
def save_sensorial_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            beer = Beer(
                name=data['name'],
                aroma=data['aroma'],
                flavor=data['flavor'],
                color=data['color'],
                texture=data['texture'],
                overall_score=(data['aroma'] + data['flavor'] + data['color'] + data['texture']) / 4
            )
            beer.save()
            return JsonResponse({'message': 'Datos guardados correctamente'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Método no permitido'}, status=405)

# @login_required
# def lista_cervezas(request):
#     cervezas = Cerveza.objects.all()
#     return render(request, 'cervezas.html', {'cervezas': cervezas})
