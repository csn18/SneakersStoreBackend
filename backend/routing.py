from django.urls import re_path

from Shop.consumers import SyncProductsConsumer

websocket_urlpatterns = [
    re_path(r'connection/', SyncProductsConsumer.as_asgi()),
]
