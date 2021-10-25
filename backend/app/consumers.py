# rest/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class NotifyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['username']
        self.room_group_name = 'notify_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from room group
    async def message(self, event):
        # Send message to WebSocket
        await self.send(text_data=json.dumps(event))
    
    async def progress(self, event):
        # Send message to WebSocket
        await self.send(text_data=json.dumps(event))
