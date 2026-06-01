from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Conversacion  # ajusta el nombre si es diferente

class LoginTest(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
    
    def test_login_correcto(self):
        response = self.client.post('/login/', {
            'username': 'testuser',
            'password': 'testpass123'
        })
        self.assertEqual(response.status_code, 302)
    
    def test_login_incorrecto(self):
        response = self.client.post('/login/', {
            'username': 'testuser',
            'password': 'wrongpass'
        })
        self.assertEqual(response.status_code, 200)


class ConversacionTest(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser2',
            password='testpass123'
        )
        self.client.login(username='testuser2', password='testpass123')
    
    def test_crear_conversacion(self):
        response = self.client.post('/chat/nueva/', {
            'titulo': 'Test chat'
        })
        self.assertEqual(response.status_code, 302)
class ChatTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser3',
            password='testpass123'
        )
        self.client.login(username='testuser3', password='testpass123')
        self.conv = Conversacion.objects.create(
            usuario=self.user,
            titulo='Test'
        )

    def test_enviar_mensaje(self):
        response = self.client.post(f'/chat/{self.conv.id}/', {
            'mensaje': 'Hola'
        })
        self.assertEqual(response.status_code, 200)
