
# ENTREGA CONVOCATORIA JUNIO

# Entrega practica

## Datos
* Nombre: Raúl Molina López
* Titulación: Telemática
* Cuenta en laboratorios: molilobo
* Cuenta URJC: r.molina.2020@alumnosurjc.es
* Vídeo básico (URL): [PENDIENTE]
* Vídeo parte opcional (URL): [PENDIENTE]
* Despliegue (URL): https://final-chatia.onrender.com
* Usuarios y contraseñas:
  * pepe / 12345678p
  * juan / 12345678ju
* Cuenta Admin Site: molilobo / 1234

---

## Recursos y métodos HTTP

* Recurso: `/` — Métodos: GET
* Recurso: `/login/` — Métodos: GET, POST
* Recurso: `/logout/` — Métodos: POST
* Recurso: `/chat/` — Métodos: GET
* Recurso: `/chat/nueva/` — Métodos: POST
* Recurso: `/chat/<id>/` — Métodos: GET, POST
* Recurso: `/chat/<id>/renombrar/` — Métodos: POST
* Recurso: `/perfil/` — Métodos: GET, POST
* Recurso: `/ayuda/` — Métodos: GET
* Recurso: `/api/chats/` — Métodos: GET (JSON)

---

## Resumen parte obligatoria

ChatIA es una aplicación web de chat conversacional desarrollada con Django que permite a usuarios autenticados interactuar con un modelo de lenguaje externo (NVIDIA API).

**Funcionalidades implementadas:**

- **Autenticación completa**: login/logout con redirección, sesiones con cookies. Acceso sin login redirige a `/login/`. Login incorrecto devuelve 401.
- **Chat funcional**: el usuario envía un prompt y recibe respuesta del LLM (NVIDIA API). El historial se guarda de forma persistente en SQLite.
- **Gestión de conversaciones**: sidebar con lista de conversaciones del usuario, creación de nueva conversación, recuperación de conversaciones previas.
- **HTMX**: usado para el refresco dinámico del chat sin recargar la página completa.
- **Perfil de usuario**: página con configuración propia (alias, preferencias).
- **Página de ayuda**: documentación general de la app, estructura y créditos.
- **Footer con métricas globales**: muestra conversaciones totales, mensajes totales, conversaciones del usuario y mensajes del usuario.
- **Header**: visible en todas las páginas con nombre del sitio (ChatIA) y usuario autenticado.
- **Menú de navegación**: visible en todas las páginas, no muestra enlace a la página actual.
- **Admin Site**: todas las tablas accesibles desde `/admin`. Usuario admin: molilobo.
- **Endpoint JSON**: `/api/chats/` devuelve lista de conversaciones del usuario en formato JSON.
- **Tests**: tests end-to-end para login, chat y creación de conversación.
- **Deploy**: aplicación desplegada en Render y accesible en Internet.
- **Favicon**: icono personalizado visible en el navegador.

---

## Lista partes opcionales

* Nombre parte: Renombrar conversaciones — permite al usuario editar el título de cualquier conversación desde el sidebar.
* Nombre parte: Favicon — icono personalizado de la aplicación visible en la pestaña del navegador.