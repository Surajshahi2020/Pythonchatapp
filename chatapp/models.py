from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name}"


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE,related_name="ms")
    sender = models.CharField(max_length=255)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.sender}"
