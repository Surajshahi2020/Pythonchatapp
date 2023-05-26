from django.urls import path
from . import views

urlpatterns = [
    path("create-room", views.create_room, name="create_room"),
    path("rooms", views.room_list, name="room_list"),
    path("rooms/<int:room_id>", views.room_detail, name="room_detail"),
    path("rooms/<int:room_id>/send/", views.send_message, name="send_message"),
]
