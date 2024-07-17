from rest_framework import generics, viewsets
from django.contrib.auth.decorators import login_required
from .models import ChatRoom, Message
from django.contrib.auth.models import User
from .serializers import UserProfileSerializer, ChatRoomSerializer, MessageSerializer
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegistrationForm

class ChatRoomViewSet(viewsets.ModelViewSet):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Account created for {user.username}!')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    return render(request, 'home/home.html', {'username': request.user.username})

# # views.py
# from rest_framework import generics, viewsets
# from django.contrib.auth.decorators import login_required
# from .models import ChatRoom, Message
# from django.contrib.auth.models import User
# from .serializers import UserProfileSerializer, ChatRoomSerializer, MessageSerializer
# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
# from .forms import UserRegistrationForm
#
# class ChatRoomViewSet(viewsets.ModelViewSet):
#     queryset = ChatRoom.objects.all()
#     serializer_class = ChatRoomSerializer
#
# class MessageViewSet(viewsets.ModelViewSet):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer
#
# class UserProfileViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserProfileSerializer
# # class UserProfileListAPIView(generics.ListAPIView):
# #     queryset = UserProfile.objects.all()
# #     serializer_class = UserProfileSerializer
# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             User.objects.create(user=user,email=form.cleaned_data.get('email'))
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}!')
#             return redirect('home')
#     else:
#         form = UserRegistrationForm()
#     return render(request, 'registration/register.html', {'form': form})
#
# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             messages.error(request, 'Invalid username or password.')
#     return render(request, 'login/login.html')
#
# def user_logout(request):
#     logout(request)
#     return redirect('login')
#
#
# @login_required
# def home(request):
#     return render(request, 'home/home.html', {'username': request.user.username})







# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             auth_login(request, user)  # Log in the user after registration
#             return redirect('home')  # Redirect to homepage or any other page after registration
#     else:
#         form = UserCreationForm()
#     return render(request, 'registration/register.html', {'form': form})
#
#
# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#             else:
#                 messages.error(request, 'Invalid username or password.')
#         else:
#             messages.error(request, 'Invalid username or password.')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login/login.html', {'form': form})
#
#
# @login_required
# def home(request):
#     return render(request, 'home/home.html')
#
# def logout_view(request):
#     auth_logout(request)
#     messages.info(request, "You have been logged out.")  # Optional: Display logout message
#     return redirect('login')  # Redirect to login page after logout
#
#
# def sumNumbers(start_num, end_num):
#     if start_num > end_num:
#         start_num, end_num = end_num, start_num
#     sum = 0
#     for i in range(start_num, end_num + 1):
#         sum += i
#     return sum
#
#
# @api_view(['Post'])
# def sumNumbersView(request):
#     if request.method == 'POST':
#         start_num = request.data['start_num']
#         end_num = request.data['end_num']
#         result = sumNumbers(start_num, end_num)
#         return Response({'result': result})
#
