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
        self.send('{"type":"accept" , "status":"accepted"}')  # Send a welcome message
        print(self.scope.get("user"))
        # print(self.scope.get("session"))
        # add id, firstname, and last name and email to the console
        print(self.scope.get("user").id)
        print(self.scope.get("user").first_name)
        print(self.scope.get("user").last_name)
        print(self.scope.get("user").email)

    def receive(self, text_data=None, bytes_data=None):
        """
        Called when a message is received from the WebSocket.
        """
        # Here you can handle incoming messages
        print("Message received:", text_data)
        self.send('{"type":"event_arrive" , "status":"you have a new message which is arrived!  "}')  # Send a response back to the client

    def disconnect(self, code):
        print("WebSocket disconnected with code:", code)

        print("hello, disconnecting")
