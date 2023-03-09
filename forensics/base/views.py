from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import *
from .models import *

# Create your views here.

#signing up a user
def signup(request):
    form = Signupform

    if request.method=="POST":
        form = Signupform(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            password = request.POST.get('password1')
            user = authenticate(username=username, password=password)
            messages.success(request, ("Registration successful. Please Login"))
            return redirect('login')
        else:
            messages.success(request, 'Registration not Successfull')
            return redirect('signup')

    else:
        form = Signupform()


    context = {'form':form}

    return render(request, 'signup.html', context)


#views for login page
def login_user(request):

    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ("Invalid username or password"))
            return redirect('login')

    else:

        return render(request, 'login.html')

#home page
@login_required(login_url='login')
def home(request):
    messages = Message.objects.all()
    form = Messageform
    user = request.user

    if request.method == "POST":
        message = request.POST.get("message")

        user = request.user

        data = Message(user=user, message=message)
        data.user = user
        data.save()
        
    context = {'form':form, 'messages':messages}

    return render(request, "home.html", context)

def logout_user(request):

    logout(request)
    return redirect('login')