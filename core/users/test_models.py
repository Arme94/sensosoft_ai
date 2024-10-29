import pytest
from .models import Cerveza

@pytest.mark.django_db
def test_crear_cerveza():
    cerveza = Cerveza.objects.create(
        nombre="IPA",
        aroma="Frutal",
        sabor="Amargo",
        color="Amarillo",
        textura="Suave"
    )
    assert cerveza.nombre == "IPA"
    assert cerveza.aroma == "Frutal"
