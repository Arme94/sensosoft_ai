from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser

class Cerveza(models.Model):
    nombre = models.CharField(max_length=100)
    aroma = models.CharField(max_length=255)
    sabor = models.CharField(max_length=255)
    color = models.CharField(max_length=50)
    textura = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    # Método para mostrar el nombre de la cerveza en las interfaces de Django
    def __str__(self):
        return self.nombre

    # Validación personalizada del campo color
    def clean(self):
        # Solo permitir ciertos colores
        colores_validos = ['Amarillo', 'Ámbar', 'Oscuro']
        if self.color not in colores_validos:
            raise ValidationError(f'Color inválido para la cerveza. Colores válidos: {", ".join(colores_validos)}')

    # Guardar el modelo aplicando la validación
    def save(self, *args, **kwargs):
        # Primero se llama a la validación antes de guardar
        self.clean()
        super(Cerveza, self).save(*args, **kwargs)

class Usuario(AbstractUser):
    ROL_CHOICES = [
        ('OPERARIO', 'Operario de Producción'),
        ('COORDINADOR', 'Coordinador de Calidad'),
        ('ADMIN', 'Administrador'),
    ]
    rol = models.CharField(max_length=20, choices=ROL_CHOICES)
