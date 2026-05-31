from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render ,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template.context_processors import request

from .models import Conversacion
@login_required
def chat_home(request):
    conversaciones= Conversacion.objects.filter(
        Usuario=request.user
    ).order_by('-creada')
    return render(request,"chat/chat_home.html",{'conversaciones':conversaciones}
                  )
@login_required
def nueva_conversacion(request):
    conv = Conversacion.objects.create(Usuario=request.user,titulo="Nueva Conversacion")
    return redirect('chat_detalle',id=conv.id)
@login_required
def chat_detalle(request,id):
    conv = get_object_or_404(Conversacion,id=id,Usuario=request.user)
    mensaje = conv.mensaje_set.order_by('-creada')
    return render(request,"chat/chat_detalle.html",{
        'conv':conv,
        'mensaje':mensaje})
