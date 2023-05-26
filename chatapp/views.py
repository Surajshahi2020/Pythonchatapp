from django.contrib import messages
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Room, Message
from django.utils.dateformat import format


def create_room(request):
    if request.method == "POST":
        username = request.POST.get("username")
        room = request.POST.get("room")
        if username and room:
            croom = Room(username=username, name=room)
            croom.save()
            messages.success(
                request, "Room created successfully!", extra_tags="custom-success"
            )
            return redirect(reverse("room_list"))
        else:
            messages.error(
                request,
                "Please enter both username and room!",
                extra_tags="custom-error",
            )

    return render(request, "chat/room_create.html")


def room_list(request):
    rooms = Room.objects.all()
    context = {
        "rooms": rooms,
    }
    return render(request, "chat/room_list.html", context)


def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    messages = room.ms.all()
    context = {
        "room": room,
        "messages": [
            {
                "id": f"{i.id}",
                "sender": f"{i.sender}",
                "content": f"{i.content}",
                "timestamp": format(i.timestamp, format_string="Y-M-D h:m:s"),
            }
            for i in messages
        ],
    }
    return render(request, "chat/room_detail.html", context)


def send_message(request, room_id):
    if request.method == "POST":
        room = get_object_or_404(Room, id=room_id)
        content = request.POST["content"]
        name = request.POST["name"]
        message = Message(room=room, content=content, sender=name)
        message.save()
        return redirect("room_detail", room_id=room.id)
