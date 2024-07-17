from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, register, user_login, user_logout, home, ChatRoomViewSet, MessageViewSet

from chat import views
#from chat.viewsets import ChatRoomViewSets, MessageViewSets, UserProfileViewSet

router = DefaultRouter()
router.register(r'chatrooms', ChatRoomViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'userprofiles', UserProfileViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('home/', home, name='home'),
]
# router = DefaultRouter()
# router.register(r'userprofiles', UserProfileViewSet, basename='user')
# router.register('chatroom', ChatRoomViewSets, basename='chatroom')
# router.register('message', MessageViewSets, basename='message')
#
# # urlpatterns = [
# #     path('api/userprofile', UserProfileListAPIView.as_view(),name='userprofiles'),
# #     path('api', include(router.urls)),
# #     path('register', register, name='register'),
# #     path('login', user_login, name='login'),
# #     path('logout', user_logout, name='logout'),
# #     path('home', home, name='home'),
# #  ]
# urlpatterns = [
#     path('api/userprofiles', UserProfileListAPIView.as_view(),name='userprofiles'),  # Include router URLs at root level
#     path('register/', register, name='register'),
#     path('login/', user_login, name='login'),
#     path('logout/', user_logout, name='logout'),
#     path('home/', home, name='home'),
#     # You can add more API endpoints here as needed
# ]



# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
#
# from chat import views
# from chat.views import sumNumbersView
# from chat.views import register, home, login_view
# from chat.viewsets import ChatRoomViewSets, MessageViewSets, UserViewSet
# from rest_framework import routers
# from . import views
#
#
# router = DefaultRouter()
# router.register(r'api/users', UserViewSet)
#
# urlpatterns = router.urls
#
# urlpatterns = [
#     path('api/', include(router.urls)),
#     path('api/register/', views.register, name='register'),
#     path('home/', views.home, name='home'),
#     path('login/', views.login_view, name='login'),
#     path('logout/', views.logout_view, name='logout'),
#     # You can add more API endpoints here as needed
# ]

#
# router = DefaultRouter()
# router.register('chatroom', ChatRoomViewSets, basename='chatroom')
# router.register('message', MessageViewSets, basename='message')
# router.register('user', UserProfileViewSet, basename='user')
#
# urlpatterns = router.urls
# urlpatterns = [
#
#     path('api/', include(router.urls)),
#     #path('api/userprofiles/', UserProfileListAPIView.as_view(), name='userprofiles'),
#     path('register/', views.register, name='register'),
#     path('home/', views.home, name='home'),
#     path('login/', views.user_login, name='login'),
#     path('logout/', views.user_logout, name='logout'),
#     # You can add more API endpoints here as needed
# ]

