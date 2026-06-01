from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('chat/',views.chat_home,name='chat_home'),
    path('chat/nueva/',views.nueva_conversacion,name='nueva_conversacion'),
    path('chat/<int:id>/',views.chat_detalle,name='chat_detalle'),
    path("perfil/",views.perfil,name='perfil'),
    path("ayuda/",views.ayuda,name='ayuda'),
    path('api/chats/',views.api_chats,name='api_chats'),
]