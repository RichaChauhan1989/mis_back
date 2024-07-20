
# from django.test import TestCase
# from rest_framework.test import APIClient
#
# from .models import ChatRoom
# from .serializers import ChatRoomSerializer
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class LoginViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('login')  # Replace 'login' with the actual name of your login URL
        self.home_url = reverse('home')  # Replace 'home' with the actual name of your home URL
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_login_success(self):
        response = self.client.post(self.url, {'username': self.username, 'password': self.password})
        self.assertRedirects(response, self.home_url)
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_login_failure(self):
        response = self.client.post(self.url, {'username': self.username, 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid username or password.')
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_login_get_request(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login/login.html')


class ChatRoomViewSetTest(TestCase):
    @classmethod
    def setUpTestData(self):
        # Set up data for the whole TestCase
        self.chatroom1 = ChatRoom.objects.create(name='Test Room 1')
        self.chatroom2 = ChatRoom.objects.create(name='Test Room 2')

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_list_chatrooms(self):
        response = self.client.get(reverse('chatroom-list'))
        chatrooms = ChatRoom.objects.all()
        serializer = ChatRoomSerializer(chatrooms, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_chatroom(self):
        data = {'name': 'New Test Room'}
        response = self.client.post(reverse('chatroom-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ChatRoom.objects.count(), 3)
        self.assertEqual(ChatRoom.objects.get(id=response.data['id']).name, 'New Test Room')

    def test_retrieve_chatroom(self):
        response = self.client.get(reverse('chatroom-detail', kwargs={'pk': self.chatroom1.pk}))
        chatroom = ChatRoom.objects.get(pk=self.chatroom1.pk)
        serializer = ChatRoomSerializer(chatroom)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_update_chatroom(self):
        data = {'name': 'Updated Test Room'}
        response = self.client.put(reverse('chatroom-detail', kwargs={'pk': self.chatroom1.pk}), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.chatroom1.refresh_from_db()
        self.assertEqual(self.chatroom1.name, 'Updated Test Room')

    def test_delete_chatroom(self):
        response = self.client.delete(reverse('chatroom-detail', kwargs={'pk': self.chatroom1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(ChatRoom.objects.count(), 1)




