from django.urls import path
from . import views
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('',views.home,name='home'),
    path('chat/',views.chat_home,name='chat_home'),
    path('chat/nueva/',views.nueva_conversacion,name='nueva_conversacion'),
    path('chat/<int:id>/',views.chat_detalle,name='chat_detalle'),
    path("perfil/",views.perfil,name='perfil'),
    path("ayuda/",views.ayuda,name='ayuda'),
    path('api/chats/',views.api_chats,name='api_chats'),
    path('chat/<int:id>/renombrar/', views.renombrar_conversacion, name='renombrar_conversacion'),
]