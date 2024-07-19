
from rest_framework import serializers
from django.contrib.auth.models import User
from chat.models import ChatRoom, Message


class UserProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(username=validated_data['username'], email=validated_data['email'],
                                        password=password)
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        # Update instance fields
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)

        # Save instance to apply changes
        instance.save()

        # If password is provided, set it separately to ensure it's hashed
        if password:
            instance.set_password(password)
            instance.save()

        return instance

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email']


# class UserProfileSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)
#     # id = serializers.ReadOnlyField(source='user.id')
#     # username = serializers.ReadOnlyField(source='user.username')
#     # email = serializers.ReadOnlyField(source='user.email')
#
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']
#
#     def create(self, validated_data):
#         password = validated_data.pop('password')
#         # user_data = validated_data.pop('user')
#         # user = User.objects.create(**user_data)
#         # email = validated_data.pop('email')
#         user = User.objects.create_user(username=validated_data['username'], email=validated_data['email'], password=password, **validated_data)
#         return user
#
#     def update(self, instance, validated_data):
#         user_data = validated_data.pop('user')
#         user = instance.user
#
#         instance.email = validated_data.get('email', instance.email)
#         instance.save()
#
#         user.username = user_data.get('username', user.username)
#         user.email = user_data.get('email', user.email)
#         user.save()
#
#         return instance

class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = ['id', 'name']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['text', 'chat_room', 'user']