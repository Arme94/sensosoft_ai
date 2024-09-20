from django import forms
from .models import Cerveza

class CervezaForm(forms.ModelForm):
    class Meta:
        model = Cerveza
        fields = ['nombre', 'aroma', 'sabor', 'color', 'textura']
