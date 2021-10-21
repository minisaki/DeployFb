from django.shortcuts import render
from .models import AccountFacebook

def index(request, device):
    return render(request, 'chat/room.html', {'device': device})


def room(request, room_name):
    list_acount = AccountFacebook.objects.all()
    return render(request, 'chat/index.html', {
        'room_name': room_name, 
        'list_acount': list_acount
    })

def get_group(request, facebookId):
    list_acount = AccountFacebook.objects.get(userid=facebookId)
    print(list_acount)
    return render(request, 'chat/index.html', {
        'room_name': room_name, 
        'list_acount': list_acount
    })


