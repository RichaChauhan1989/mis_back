from django.contrib.auth.models import AbstractUser, User
from django.db import models


# Create your models here.
# class CustomUser(AbstractUser):
#     pass

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     #email = models.EmailField()
#
#     def __str__(self):
#         return self.user.username


class ChatRoom(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    text = models.TextField()
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text + "-" + self.user.username
