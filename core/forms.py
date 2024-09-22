from django import forms
from .models import Cerveza
from .models import Usuario

class CervezaForm(forms.ModelForm):
    class Meta:
        model = Cerveza
        fields = ['nombre', 'aroma', 'sabor', 'color', 'textura']

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'rol']
    def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['password'].widget = forms.PasswordInput()
        self.fields['rol'].widget = forms.Select(choices=Usuario.ROL_CHOICES)
