from channels.generic.websocket import WebsocketConsumer



class ChatConsumer(WebsocketConsumer):
    """
    A WebSocket consumer for handling chat messages.
    """
    def connect(self):
        """
        Called when the WebSocket is handshaking as part of the connection process.
        """
        self.accept()  # Accept the WebSocket connection

    def disconnect(self, close_code):
        """
        Called when the WebSocket closes.
        """
        pass  # Handle disconnection if needed

    def receive(self, text_data):
        """
        Called when a message is received from the WebSocket.
        """
        # Here you can handle incoming messages
        self.send(text_data=f"Message received: {text_data}")  # Echo the message back