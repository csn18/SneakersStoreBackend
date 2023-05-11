import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class SyncProductsConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.room_group_name = None

    def connect(self):
        self.room_group_name = 'room'
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        pass

    def update_price_product(self, event):
        self.send(text_data=json.dumps(event))

    def update_cart(self, event):
        print(event)
        self.send(text_data=json.dumps(event))
