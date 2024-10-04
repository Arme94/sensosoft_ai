from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Usuario
from .forms import UsuarioForm

def users(request):
    users = Usuario.objects.all()
    return render(request, 'users/template/users.html', {'users': users})

def user_create(request):
    if request.method == 'POST':
        user_form = UsuarioForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('users')
    else:
        user_form = UsuarioForm()
    return render(request, 'users/template/user_create.html', {'user_form': user_form})

def user_detail(request, id):
    user = Usuario.objects.get(id=id)
    user_form = UsuarioForm(instance=user)
    return render(request, 'users/template/user_detail.html', {'user_form': user_form})    

def user_update(request, id):
    user = Usuario.objects.get(id=id)
    if request.method == 'POST':
        user_form = UsuarioForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            return redirect('users/template/user_detail', id=id)
    else:
        user_form = UsuarioForm(instance=user)
    
    return render(request, 'users/template/user_update.html', {'user_form': user_form})

def user_delete(request, id):
    user = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'Usuario eliminado correctamente.')
        return redirect('users')
    return render(request, 'users/template/user_delete.html', {'user': user})