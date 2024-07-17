from rest_framework import viewsets
from chat.models import ChatRoom, Message
from chat.serializers import ChatRoomSerializer, MessageSerializer, UserProfileSerializer
from django.contrib.auth.models import User

class ChatRoomViewSets(viewsets.ModelViewSet):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer

class MessageViewSets(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer

