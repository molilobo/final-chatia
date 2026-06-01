from .models import Conversacion,Mensaje
def metricas_globales(request):
    total_conversaciones = Conversacion.objects.count()
    total_mensajes = Mensaje.objects.count()

    conv_usuarios = 0
    mensa_usuarios = 0

    if request.user.is_authenticated:
        conv_usuarios = Conversacion.objects.filter(usuario=request.user).count()
        mensa_usuarios = Mensaje.objects.filter(conversacion__usuario=request.user).count()
    return {
            'total_conversaciones': total_conversaciones,
            'total_mensajes': total_mensajes,
            'conv_usuario': conv_usuarios,
            'mensa_usuario': mensa_usuarios,
    }