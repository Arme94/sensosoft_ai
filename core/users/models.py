from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    ROL_CHOICES = [
        ('OPERARIO', 'Operario de Producción'),
        ('COORDINADOR', 'Coordinador de Calidad'),
        ('ADMIN', 'Administrador'),
    ]
    rol = models.CharField(max_length=20, choices=ROL_CHOICES)
