from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, register, user_login, user_logout, home

from chat import views
#from chat.viewsets import ChatRoomViewSets, MessageViewSets, UserProfileViewSet

router = DefaultRouter()
#router.register(r'chatrooms', ChatRoomViewSet)
#router.register(r'messages', MessageViewSet)
router.register(r'userprofiles', UserProfileViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('home/', home, name='home'),
]






