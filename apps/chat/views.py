from django.shortcuts import render
from .models import Room, Message

def home(request):
    rooms = Room.objects.all()
    messages = Message.objects.all()
    return render(request, 'index.html', {
        'rooms': rooms,
        'messages': messages
    })


  