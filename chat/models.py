from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Conversacion(models.Model):
        usuario = models.ForeignKey(User, on_delete=models.CASCADE)
        titulo  = models.CharField(max_length=100)
        creada = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.titulo
class Mensaje(models.Model):
    ROL_CHOIZES = [
        ('User', 'Usuario'),
        ('assistant', 'Asistente'),
    ]
    conversacion = models.ForeignKey(Conversacion, on_delete=models.CASCADE)
    rol = models.CharField(max_length=20, choices=ROL_CHOIZES)
    contenido = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.rol}: {self.contenido[:50]}"
class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    alias = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100, default= "meta/llama-3.1-8b-instruct")
    temperatura = models.FloatField(default= 0.2)

    def __str__(self):
        return f"Perfil de {self.usuario.username}"