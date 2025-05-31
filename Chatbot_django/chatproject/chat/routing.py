"""
This file contains the URL patterns for the chat application.
"""
from django.urls import path
from . import consumers


ASGI_urlpatterns = [
    path('websocket/<str:name>' , consumers.ChatConsumer.as_asgi( )),
]
