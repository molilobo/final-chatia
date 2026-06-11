

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render ,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from openai import OpenAI
from .models import Conversacion,Mensaje,PerfilUsuario


def obtener_respuest_llm(mensaje_historial):
    client = OpenAI(
        base_url="https://integrate.api.nvidia.com/v1",
        api_key=settings.NVIDIA_API_KEY
    )
    completion = client.chat.completions.create(
        model = "meta/llama-3.1-8b-instruct",
        messages= mensaje_historial,
        temperature = 0.2,
        max_tokens=1024,
        stream=False

    )
    return completion.choices[0].message.content
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
            Mensaje.objects.create(
                conversacion = conv,
                rol= 'User',
                contenido=contenido,

            )
            #la api aqui
            historial = [
                {"role":"user" if m.rol == "User" else "assistant",
                 "content":m.contenido}
                for m in conv.mensaje_set.order_by('creado')
            ]
            respuesta = obtener_respuest_llm(historial)
            Mensaje.objects.create(
                conversacion = conv,
                rol='assistant',
                contenido=respuesta,
            )
        mensaje = conv.mensaje_set.order_by('creado')
        return render(request,"chat/mensajes_parcial.html",{
            'mensaje':mensaje
        })

    mensaje = conv.mensaje_set.order_by('creado')
    return render(request,"chat/chat_detalle.html",{
            'conv':conv,
            'mensaje':mensaje})
@login_required
def perfil(request):
    perfil, _ =PerfilUsuario.objects.get_or_create(usuario=request.user)

    if request.method == 'POST':
        perfil.alias =request.POST.get('alias', '')
        perfil.modelo = request.POST.get('modelo',perfil.modelo)
        perfil.temperatura = float(request.POST.get('temperatura',perfil.temperatura))
        perfil.save()

    return render(request,"chat/perfil.html",{'perfil': perfil})
def ayuda(request):
    return render(request,"chat/ayuda.html")
@login_required
def api_chats(request):
    conversaciones= Conversacion.objects.filter(usuario=request.user).values('id','titulo','creada')
    return JsonResponse(list(conversaciones),safe=False)
@login_required
def renombrar_conversacion(request, id):
    conv = get_object_or_404(Conversacion, id=id, usuario=request.user)
    if request.method == 'POST':
        nuevo_titulo = request.POST.get('titulo', '').strip()
        if nuevo_titulo:
            conv.titulo = nuevo_titulo
            conv.save()
    return redirect('chat_home')
    
