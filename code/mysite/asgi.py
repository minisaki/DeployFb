"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""



import os
import django
from channels.routing import get_default_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

django.setup()

application = get_default_application()

# from channels.auth import AuthMiddlewareStack
# from channels.security.websocket import AllowedHostsOriginValidator
# from channels.routing import ProtocolTypeRouter, URLRouter, ChannelNameRouter
# from chat.consumers import ChatConsumer
# from django.urls import re_path

# application = ProtocolTypeRouter({
#     'http': django_asgi_app,
#     'websocket': AllowedHostsOriginValidator(
#         AuthMiddlewareStack(
#             URLRouter(
#                 [
#                     re_path(r'ws/chat/(?P<room_name>\w+)/$', ChatConsumer.as_asgi()),
#                 ]
#             )
#         )
#     ),
    
# })
