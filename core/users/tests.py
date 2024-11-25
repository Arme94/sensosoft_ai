from django.test import TestCase
from django.urls import reverse
from core.users.models import Usuario

# Create your tests here.

class UsuarioTests(TestCase):

    def setUp(self):
    
        # Crea un usuario con rol de Operario
        self.operario = Usuario.objects.create_user(
            username='operario1',
            password='pass12345',
            rol='OPERARIO',
            first_name='Operario',
            last_name='Uno',
            email='operario1@test.com'
        )

        # Crea un usuario con rol de Coordinador de Calidad
        self.coordinador = Usuario.objects.create_user(
            username='coordinador1',
            password='pass12345',
            rol='COORDINADOR',
            first_name='Coordinador',
            last_name='Uno',
            email='coordinador1@test.com'
        )

        # Crea un usuario con rol de Administrador
        self.admin = Usuario.objects.create_user(
            username='admin1',
            password='pass12345',
            rol='ADMIN',
            first_name='Admin',
            last_name='Uno',
            email='admin1@test.com'
        )

    def test_crear_usuario(self):
       
        self.assertEqual(self.operario.username, 'operario1')
        self.assertEqual(self.operario.rol, 'OPERARIO')
        self.assertEqual(self.coordinador.rol, 'COORDINADOR')
        self.assertEqual(self.admin.rol, 'ADMIN')

    def test_editar_usuario(self):
      
        self.operario.first_name = 'OperarioEditado'
        self.operario.save()

        usuario_editado = Usuario.objects.get(username='operario1')
        self.assertEqual(usuario_editado.first_name, 'OperarioEditado')

    def test_eliminar_usuario(self):
     
        self.coordinador.delete()
        with self.assertRaises(Usuario.DoesNotExist):
            Usuario.objects.get(username='coordinador1')

    def test_lista_usuarios(self):
     
        usuarios = Usuario.objects.all()
        self.assertEqual(usuarios.count(), 3)

    def test_usuario_rol(self):
       
        self.assertEqual(self.operario.rol, 'OPERARIO')
        self.assertEqual(self.coordinador.rol, 'COORDINADOR')
        self.assertEqual(self.admin.rol, 'ADMIN')

    def test_creacion_usuario_desde_form(self):
        
        data = {
            'username': 'nuevo_usuario',
            'password1': 'pass12345',
            'password2': 'pass12345',
            'first_name': 'Nuevo',
            'last_name': 'Usuario',
            'email': 'nuevo@test.com',
            'rol': 'OPERARIO'
        }
        response = self.client.post(reverse('user_create'), data)
        self.assertEqual(response.status_code, 302)  # Redirección después de la creación
        nuevo_usuario = Usuario.objects.get(username='nuevo_usuario')
        self.assertEqual(nuevo_usuario.first_name, 'Nuevo')
        self.assertEqual(nuevo_usuario.rol, 'OPERARIO')