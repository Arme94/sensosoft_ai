from django.contrib import admin
from .models import Cerveza

@admin.register(Cerveza)
class CervezaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'aroma', 'sabor', 'color', 'textura', 'fecha_creacion')

