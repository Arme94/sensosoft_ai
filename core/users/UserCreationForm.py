from django import forms
from .models import Usuario
from core.role.models import Role
from django.contrib.auth.forms import UserCreationForm

class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'rol', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UsuarioCreationForm, self).__init__(*args, **kwargs)
        self.fields['rol'].queryset = Role.objects.all()
        self.fields['rol'].widget = forms.Select(choices=[(role.id, role.name) for role in Role.objects.all()])

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control required-field'
            field.widget.attrs['placeholder'] = field.label