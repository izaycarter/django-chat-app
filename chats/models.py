from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class Room(models.Model):
    name = models.CharField(max_length=255)
    member = models.ManyToManyField( User ,related_name="rooms")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("chats:room_list")




class Comment(models.Model):
    text = models.TextField( max_length=500)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
