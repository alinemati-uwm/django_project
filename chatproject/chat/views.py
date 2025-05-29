from django.shortcuts import render
from django.views import View

# Create your views here.

class Main(View):
    def get(self, request):
        """
        Render the main page of the chat application.
        """
        return render(request, template_name='chat/main.html')

class Home(View):
    def get(self, request):
        """
        Render the home page of the chat application.
        """
        return render(request, template_name='chat/home.html')

class Login(View):
    def get(self, request):
        """
        Render the login page.
        """
        return render(request, template_name='chat/login.html')

class Register(View):
    def get(self, request):
        """
        Render the registration page.
        """
        return render(request, template_name='chat/register.html')

class Chat(View):
    def get(self, request):
        """
        Render the chat page.
        """
        return render(request, template_name='chat/chat.html')


class Logout(View):
    def get(self, request):
        pass


class ChatPerson(View):
    def get(self, request):
        """
        Render the chat with a specific person.
        """
        # Logic to retrieve the person to chat with can be added here
        return render(request, template_name='chat/chat_person.html')
    