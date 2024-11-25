from django import forms
from .models import Cerveza

# class CervezaForm(forms.ModelForm):
#     class Meta:
#         model = Cerveza
#         fields = ['nombre', 'aroma', 'sabor', 'color', 'textura']
#         labels = {
#             'nombre': 'Nombre de la Cerveza',
#             'aroma': 'Aroma',
#             'sabor': 'Sabor',
#             'color': 'Color',
#             'textura': 'Textura',
#         }
#         widgets = {
#             'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la cerveza'}),
#             'aroma': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripción del aroma'}),
#             'sabor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripción del sabor'}),
#             'color': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Color de la cerveza'}),
#             'textura': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Textura'}),
#         }


#     def clean_nombre(self):
#         nombre = self.cleaned_data.get('nombre')
#         if not nombre:
#             raise forms.ValidationError("El nombre de la cerveza es obligatorio.")
#         if len(nombre) < 3:
#             raise forms.ValidationError("El nombre debe tener al menos 3 caracteres.")
#         return nombre
