

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render ,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from openai import OpenAI
from .models import Conversacion,Mensaje


def obtener_respuest_llm(mensaje_historial):
    client = OpenAI(
        base_url="https:///integrate.api.nvidia.com",
        api_key=settings.NVIDIA_API_KEY
    )
    comletion = client.chat.completions.create(
        model = "met/llama-3.1-8b--instruct",
        messages= mensaje_historial,
        temperature = 0.2,
        max_tokens=1024,
        stream=False

    )
    return comletion.choices[0].message.content
def home(request):
    return render(request,"chat/home.html")
@login_required
def chat_home(request):
    conversaciones= Conversacion.objects.filter(
        usuario=request.user
    ).order_by('-creada')
    return render(request,"chat/chat_home.html",{
        'conversaciones':conversaciones
    })
@login_required
def nueva_conversacion(request):
    conv = Conversacion.objects.create(usuario=request.user,titulo="Nueva Conversacion")
    return redirect('chat_detalle',id=conv.id)

@login_required
def chat_detalle(request,id):
    conv = get_object_or_404(Conversacion,id=id,usuario=request.user)

    if request.method == 'POST':
        contenido = request.POST.get('mensaje', '').strip()
        print("contenido",contenido)
        if contenido :
            m =  Mensaje.objects.create(
                conversacion = conv,
                rol= 'User',
                contenido=contenido,

            )
    #la api aqui
        historial = [
            {"role":"user"if m.rol == "User" else "assistant",
             "content":m.contenido}
            for m in conv.mensaje_set.order_by('-creado')
        ]
        respuesta = obtener_respuest_llm(historial)
        Mensaje.objects.create(
            conversacion = conv,
            rol='assistant',
            contenido=respuesta,
        )
        return redirect('chat_detalle',id=conv.id)
    mensaje = conv.mensaje_set.order_by('-creado')
    return render(request,"chat/chat_detalle.html",{
            'conv':conv,
            'mensaje':mensaje})
