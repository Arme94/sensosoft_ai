from django.urls import reverse
import pytest

@pytest.mark.django_db
def test_user_login(client, django_user_model):
    # Crear un usuario de prueba
    username = "testuser"
    password = "testpassword"
    django_user_model.objects.create_user(username=username, password=password)

    # Hacer la petición de login
    response = client.post(reverse('login'), {'username': username, 'password': password})
    
    # Verificar redirección después del login
    assert response.status_code == 302  # Redirige al login
    assert response.url == reverse('home')
