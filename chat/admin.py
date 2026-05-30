from django.contrib import admin

# Register your models here.
from .models import Conversacion,Mensaje
admin.site.register(Conversacion)
admin.site.register(Mensaje)