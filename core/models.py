from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser

# class Cerveza(models.Model):
#     nombre = models.CharField(max_length=100)
#     aroma = models.CharField(max_length=255)
#     sabor = models.CharField(max_length=255)
#     color = models.CharField(max_length=50)
#     textura = models.CharField(max_length=255)
#     fecha_creacion = models.DateTimeField(auto_now_add=True)

#     # Método para mostrar el nombre de la cerveza en las interfaces de Django
#     def __str__(self):
#         return self.nombre

#     # Validación personalizada del campo color
#     def clean(self):
#         # Solo permitir ciertos colores
#         colores_validos = ['Amarillo', 'Ámbar', 'Oscuro']
#         if self.color not in colores_validos:
#             raise ValidationError(f'Color inválido para la cerveza. Colores válidos: {", ".join(colores_validos)}')

#     # Guardar el modelo aplicando la validación
#     def save(self, *args, **kwargs):
#         # Primero se llama a la validación antes de guardar
#         self.clean()
#         super(Cerveza, self).save(*args, **kwargs)
        
class Beer(models.Model):
    name = models.CharField(max_length=100)
    aroma = models.FloatField()
    flavor = models.FloatField()
    color = models.FloatField()
    texture = models.FloatField()
    overall_score = models.FloatField()

    def __str__(self):
        return self.name

    @staticmethod
    def get_average_sensory_data():
        beer_names = ['carmesi', 'lecter', 'sauer', 'prendida', 'tramadora', 'la 10']
        data = {
            'labels': beer_names,
            'aroma': [],
            'flavor': [],
            'color': [],
            'texture': []
        }
        for name in beer_names:
            beers = Beer.objects.filter(name=name)
            if beers.exists():
                data['aroma'].append(beers.aggregate(models.Avg('aroma'))['aroma__avg'])
                data['flavor'].append(beers.aggregate(models.Avg('flavor'))['flavor__avg'])
                data['color'].append(beers.aggregate(models.Avg('color'))['color__avg'])
                data['texture'].append(beers.aggregate(models.Avg('texture'))['texture__avg'])
            else:
                data['aroma'].append(0)
                data['flavor'].append(0)
                data['color'].append(0)
                data['texture'].append(0)
        return data

class SensoryEvaluation(models.Model):
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE)
    evaluator_name = models.CharField(max_length=100)
    evaluation_date = models.DateField(auto_now_add=True)
    comments = models.TextField()

    def __str__(self):
        return f"Evaluation of {self.beer.name} by {self.evaluator_name}"

