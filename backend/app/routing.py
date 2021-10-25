# notify/routing.py
from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'notify/(?P<username>\w+)/$', consumers.NotifyConsumer.as_asgi()),
]
