from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Usuario
from .UserCreationForm import UsuarioCreationForm
from .UserChangeForm import UsuarioChangeForm
from django.contrib.auth import authenticate, login
from django.contrib.messages import get_messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

def user_login(request):
    storage = get_messages(request)
    for _ in storage:
        pass

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('users/template/users.html')  # Cambia 'home' por la ruta a donde quieres redirigir tras el login
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'users/template/login.html')

def users(request):
    users = Usuario.objects.all()
    return render(request, 'users/template/users.html', {'users': users})

def user_create(request):
    if request.method == 'POST':
        user_form = UsuarioCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('users')
    else:
        user_form = UsuarioCreationForm()
    return render(request, 'users/template/user_create.html', {'user_form': user_form})

def user_detail(request, id):
    user = get_object_or_404(Usuario, id=id)

    storage = get_messages(request)
    for _ in storage:
        pass

    user_form = UsuarioChangeForm(instance=user)
    return render(request, 'users/template/user_detail.html', {'user_form': user_form})    

def user_update(request, id):
    user = get_object_or_404(Usuario, id=id)

    if request.method == 'POST':
        user_form = UsuarioChangeForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Usuario actualizado correctamente.')
            return redirect('user_detail', id=id)
    else:
        user_form = UsuarioChangeForm(instance=user)
    
    return render(request, 'users/template/user_update.html', {'user_form': user_form})

def user_delete(request, id):
    user = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'Usuario eliminado correctamente.')
        return redirect('users')
    return render(request, 'users/template/user_delete.html', {'user': user})

def update_user_info(request, id):
    user = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        password_form = PasswordChangeForm(request.user, request.POST)
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Contraseña actualizada correctamente.')
            return render(request, 'users/template/update_user_info.html', {'password_form': password_form, 'success': True})
        else:
            messages.error(request, 'Por favor corrige los errores a continuación.')
    else:
        password_form = PasswordChangeForm(request.user)
    
    # Add CSS classes to form fields
    for field in password_form.fields.values():
        field.widget.attrs['class'] = 'form-control required-field'
    
    return render(request, 'users/template/update_user_info.html', {'password_form': password_form})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Tu contraseña ha sido actualizada exitosamente.')
            return redirect('users')
        else:
            messages.error(request, 'Por favor corrige los errores a continuación.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/template/update_user_info.html', {'form': form})