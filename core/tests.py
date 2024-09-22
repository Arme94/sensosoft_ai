from django.test import TestCase
from .models import Cerveza

class CervezaTestCase(TestCase):
    def setUp(self):
        Cerveza.objects.create(nombre="Test Cerveza", aroma="Frutal", sabor="Dulce", color="Ámbar", textura="Suave")

    def test_cerveza_creacion(self):
        cerveza = Cerveza.objects.get(nombre="Test Cerveza")
        self.assertEqual(cerveza.sabor, "Dulce")

