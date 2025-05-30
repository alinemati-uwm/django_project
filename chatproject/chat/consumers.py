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
        # Send a welcome message
        self.send('{"type":"accept" , "status":"accepted"}')

        print(self.scope.get("url_route"))

        print(self.scope.get("url_route").get("kwargs").get("name"))

        {"args": (), "kwargs": {"name": "Mohammad"}}

        # Print user information
        if self.scope.get("user"):
            print(self.scope.get("user"))
            print(f"User ID: {self.scope.get('user').id}")
            print(f"First Name: {self.scope.get('user').first_name}")
            print(f"Last Name: {self.scope.get('user').last_name}")
            print(f"Email: {self.scope.get('user').email}")

        # Print session information
        if self.scope.get("session"):
            print("Session data:", self.scope.get("session"))
            session_value = self.scope.get(
                "session").get("get_me_from_the_consumer")
            print("Session value 'get_me_from_the_consumer':", session_value)
        else:
            print("No session found in scope")


        print(self.channel_layer)
        print(type(self.channel_layer))


    def receive(self, text_data=None, bytes_data=None):
        """
        Called when a message is received from the WebSocket.
        """
        # Here you can handle incoming messages
        print("Message received:", text_data)
        # Send a response back to the client
        self.send(
            '{"type":"event_arrive" , "status":"you have a new message which is arrived!  "}')

    def disconnect(self, code):
        print("WebSocket disconnected with code:", code)

        print("hello, disconnecting")
