"""
ASGI config for wechat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from mychat.routing import websocket_urlpatterns

# Set the default Django settings module for the 'asgi' command.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wechat.settings')

# Create an ASGI application instance.
application = ProtocolTypeRouter({
    # HTTP (Django's default)
    "http": get_asgi_application(),

    # WebSocket
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})



