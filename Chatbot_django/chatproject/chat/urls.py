"""
This file contains the URL patterns for the chat application.
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('' , views.Main.as_view() , name='main'),
    path('login/',views.Login.as_view() , name='login'),
    path('register/', views.Register.as_view() , name='register'),
    path('chat/', views.Chat.as_view() , name='chat'),
    path('logout/', views.Logout.as_view() , name='logout'),
    path('chat_person/', views.ChatPerson.as_view() , name='chat_person'),
    path('home/', views.Home.as_view() , name='home'),


]