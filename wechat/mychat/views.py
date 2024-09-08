from django.shortcuts import render
from django.contrib.auth.models import User  
from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


# Create your views here.
def index(request):
    return render(request, 'index.html')

def login_user(request):
    return render(request, 'account/login.html')

@login_required
def chat(request, id):
    all_chats = (Chat.objects.filter(sender=request.user, receiver=User.objects.get(id=id)) | Chat.objects.filter(receiver=request.user, sender=User.objects.get(id=id))).order_by('-created')   
    all_users = User.objects.exclude(username= request.user.username)
    other_user = get_object_or_404(User, id=id)
    room_name = generate_room_name(request.user.id, id)
    return render(request, 'chat.html', {'all_users': all_users,'all_chats': all_chats, 'other_user': other_user, 'room_name': str(room_name)})

@login_required
def friends(request):
    all_users = User.objects.exclude(username= request.user.username)
    return render(request, 'friends.html', {'all_users': all_users})

def generate_room_name(sender_id, receiver_id):
    sorted_ids = sorted([sender_id, receiver_id])
    return f"room_{sorted_ids[0]}_{sorted_ids[1]}"