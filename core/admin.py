from django.contrib import admin

from core.users.models import Usuario
from .models import Cerveza

@admin.register(Cerveza)
class CervezaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'aroma', 'sabor', 'color', 'textura', 'fecha_creacion')
    search_fields = ('nombre', 'aroma', 'sabor')
    list_filter = ('color', 'textura', 'fecha_creacion')

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'rol', 'is_active', 'date_joined')
    search_fields = ('username', 'email')
    list_filter = ('rol', 'is_active', 'date_joined')