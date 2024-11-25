from django.db import models
from django.contrib.auth.models import AbstractUser
from core.role.models import Role
from django.utils.translation import gettext_lazy as _
from six import text_type

class Usuario(AbstractUser):
    rol = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=True, default=2)
    first_name = models.CharField(
        _("Nombre"),
        max_length=150,
        blank=False,
    )

    last_name = models.CharField(
        _("Apellidos"),
        max_length=150,
        blank=False,        
    )    
    email = models.EmailField(
        _("Correo electrónico"),
        unique=True,
        blank=False,
    )
    
    def __str__(self):
        return self.name
    
    @property
    def first_name_help_text(self):
        return text_type(self._meta.get_field('first_name').help_text)