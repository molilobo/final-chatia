from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Conversacion(models.Model):
        Usuario = models.ForeignKey(User, on_delete=models.CASCADE)
        titulo  = models.CharField(max_length=100)
        creada = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.titulo
class Mensaje(models.Model):
    ROL_CHOIZES = [
        ('User', 'Usuario'),
        ('asistant', 'Asistente'),
    ]
    conversacion = models.ForeignKey(Conversacion, on_delete=models.CASCADE)
    rol = models.CharField(max_length=1, choices=ROL_CHOIZES)
    contenido = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.rol}: {self.contenido[:50]}"