from django.urls import path
from . import views
urlpatterns = [
    path('chat/',views.chat_home,name='chat_home'),
    path('chat/nueva/',views.nueva_conversacion,name='nueva_conversacion'),
    path('chat/<int:id>/',views.chat_detalle,name='chat_detalle')
]